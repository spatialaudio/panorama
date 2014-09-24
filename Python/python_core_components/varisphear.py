import schunk
import serial
import math
from sys import stderr
import os
from python_core_components.panorama_calculation import PanoramaCalculator
from time import sleep
import subprocess


class VariSphear:

    ''' Offers functions for taking picture 
        with the VariSphear '''

    def __init__(self, port_top, port_base):
        self.calc = PanoramaCalculator()
        self.port_top = port_top
        self.port_base = port_base

    def map_motor_top(self, angle_v):
        '''Creates a List containing the motorposition
         for each vertical stage.'''

        # Number of vertical Stages
        NumStages = int(self.calc.calc_num_stages(angle_v))

        # create List for vertical motorpositions
        li_motorTop = []

        '''# "NumStages*motor_step" should be 180°.
            In the Specialcase that 180%angle_v==0 ,
            motor_step and angle_v are equal.
            Otherwise we have rounded up in Fkt "calcNumStages(..)"
            and there will be a overlap between adjacent pictures.'''

        motor_step = round(180.0 / NumStages, 2)

        # Start with the top stage and consider symmetry of aperture angle
        max_Vposition = 90
        start = max_Vposition - motor_step * 0.5

        for stage in range(NumStages):
            # Positions between 90° and -90°
            position = float(start) - float(motor_step) * float(stage)
            li_motorTop.append(round(position, 2))

        '''# We want to shift the overlap towards MotorPosition 0°
            because this will increase the benefit of the overlap.
            1/2 Overlap per Picture ( symmetric ):'''

        HalfOverlapPicture = 0.5 * (angle_v - (180 / NumStages))

        for index, position in enumerate(li_motorTop):

            if(position > 0):
                li_motorTop[index] = position - HalfOverlapPicture

            elif(position < 0):
                li_motorTop[index] = position + HalfOverlapPicture

        #print("\n Motor Positions Vertikal" + str(li_motorTop))

        return li_motorTop

    def map_motor_base(self, angle_h):
        ''' Creates a List containing the motorposition
         for each horizontal step/picture .'''

        # start Position is at 0°
        start = 0

        # Number of Steps per Rotation
        RotationSteps = int(self.calc.calc_steps_rotation(angle_h))

        '''# "RotationSteps*motor_step" should be 360° (just one Rotation).
        In the Specialcase that 360%angle_h==0 ,
        motor_step and angle_h are equal.
        Otherwise we have rounded up in Fkt "calcStepsRotation(..)"
        and there will be a overlap between adjacent pictures.'''

        motor_step = round(360.0 / RotationSteps, 2)

        # create List for horizontal motorpositions
        li_motorBase = []

        for step in range(RotationSteps):
            # Positions between 0° and 360°
            position = start + motor_step * float(step)
            li_motorBase.append(round(position, 2))

        #print("\n Motor Positions Horizontal" + str(li_motorBase))

        return li_motorBase

    def taking_pictures(self, li_motorTop, li_motorBase, dir_output, path_cfg):
        # Drive to all motorposition in li_motorTop and li_motorBase.

        # Init motor
        try:
            # "top" indicate the motor,
            #   which is responsible for the vertical rotation
            top = schunk.Module(schunk.SerialConnection(
                0x0B,
                serial.Serial,
                port=self.port_top,
                baudrate=9600,
                timeout=None))

            if(not top.toggle_impulse_message()):
                top.toggle_impulse_message()
        except:
            stderr.write('''\nERROR @takingPicture by
                 connecting to top schunkModul''')
            exit()

        try:
                # "base" indicate the motor,
                #   which is responsible for the horizontal rotation
            base = schunk.Module(schunk.SerialConnection(
                0x0B,
                serial.Serial,
                port=self.port_base,
                baudrate=9600,
                timeout=None))

            if(not base.toggle_impulse_message()):
                base.toggle_impulse_message()
        except:
            stderr.write('''\nERROR @takingPicture
                 by connecting to base schunkModul''')
            exit()

        li_prefix = list(map(chr, range(97, 123)))

        for index_v, pos_v in enumerate(li_motorTop):

            top.move_pos_blocking(pos_v)
            prefix = li_prefix[index_v]

            for index_h, pos_h in enumerate(li_motorBase):
                base.move_pos_blocking(pos_h)

                filename = dir_output + '/' + \
                    prefix + "_" + str(index_h) + ".jpg"

                # take a picture on each step
                self.trigger_cam(filename, 5)

                print("\n" + filename)

    def trigger_cam(self, filename, wait):
        # Triggers the Cam using the cmd-tool of gphoto2 and download+save the
        # picture in 'filename'
        print("\n click")

        cmd = "gphoto2 --capture-image-and-download --keep --force-overwrite --filename " + \
            filename + " "

        # subprocess call
        # subprocess Popen
        print(cmd)

        try:
            subprocess.check_call(
                ["gphoto2", "--capture-image-and-download", "--keep", "--force-overwrite", "--filename", filename])
        except SystemError as error:

            raise RuntimeError(''' Orignal Error : ''' + str(error) +
                               '''\n \nMake sure that gphoto2 is correct installed.''')

        # sleep(wait)
