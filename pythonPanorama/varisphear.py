# -*- coding: utf-8 -*-
#import schunk
#import serial
import math
from sys import stderr
import os
from pythonPanorama.panoramaCalculation import panoramaCalculation

class varisphear:
    def __init__(self):
        self.calc=panoramaCalculation()

    def mapMotorTop(self,angle_v):
        # Creates a List containing the motorposition for each vertical stage.
        # 
        
        # Number of vertical Stages
        NumStages=int(self.calc.calcNumStages(angle_v));

        # create List for vertical motorpositions
        li_motorTop=[];

        # "NumStages*motor_step" should be 180°.
        # In the Specialcase that 180%angle_v==0 ,  motor_step and angle_v are equal.
        # Otherwise we have rounded up in Fkt "calcNumStages(..)" and there will be a overlap between adjacent pictures.

        motor_step=round(180.0/NumStages,2);
        
        # Start with the top stage and consider symmetry of aperture angle
        max_Vposition=90;
        start=max_Vposition-motor_step*0.5;
        
     
        for stage in range(NumStages):
        # Positions between 90° and -90°
            position=float(start)-float(motor_step)*float(stage);
            li_motorTop.append(round(position,2));


        print("\n Motor Positions Vertikal"+str(li_motorTop));

        # We want to shift the overlap towards MotorPosition 0° because this will increase the benefit of the overlap.
        # 1/2 Overlap per Picture ( symmetric ):

        HalfOverlapPicture=0.5*(angle_v-(180/NumStages))

        
        for index,position in enumerate(li_motorTop):

            if(position>0):
                li_motorTop[index]=position-HalfOverlapPicture;

            elif(position<0):
                li_motorTop[index]=position+HalfOverlapPicture;
        
        

        print("\n Motor Positions Vertikal"+str(li_motorTop));

        
        return li_motorTop

    def mapMotorBase(self,angle_h):
        # Creates a List containing the motorposition for each horizontal step/picture .
        # 
        
        # start Position is at 0°
        start=0;
        
        # Number of Steps per Rotation
        RotationSteps=int(self.calc.calcStepsRotation(angle_h));    
        
        # "RotationSteps*motor_step" should be 360° (just one Rotation).
        # In the Specialcase that 360%angle_h==0 ,  motor_step and angle_h are equal.
        # Otherwise we have rounded up in Fkt "calcStepsRotation(..)" and there will be a overlap between adjacent pictures.
        motor_step=round(360.0/RotationSteps,2);
        

        # create List for horizontal motorpositions
        li_motorBase=[]

        for step in range(RotationSteps):
        # Positions between 0° and 360°
            position=start+motor_step*float(step);
            print(str(position));
            li_motorBase.append(round(position,2));
        
        return li_motorBase


    def takingPictures(self,li_motorTop,li_motorBase,dir_output,path_cfg):
        # Drive to all motorposition in li_motorTop and li_motorBase.

    # Init motor
    #try:
    # "top" indicate the motor, which is responsible for the vertical rotation   
    #top = schunk.Module(schunk.SerialConnection(
    #    0x0B, serial.Serial, port='COM2', baudrate=9600, timeout=None))
    #if(not top.toggle_impulse_message()):
    #    top.toggle_impulse_message();
    #except:
    #    stderr.write("\nERROR @takingPicture by connecting to top schunkModul")
    #    exit()

    # "base" indicate the motor, which is responsible for the horizontal rotation   
    #base = schunk.Module(schunk.SerialConnection(
    #    0x0B, serial.Serial, port='COM1', baudrate=9600, timeout=None))
    #if(not base.toggle_impulse_message()):
    #    base.toggle_impulse_message();  
    #except:
    #    stderr.write("\nERROR @takingPicture by connecting to base schunkModul")
    #    exit()
        
        for index_v,pos_v in enumerate(li_motorTop):
            #top.move_pos_blocking(pos_v)

            for index_h,pos_h in enumerate(li_motorBase):
                #base.move_pos_blocking(pos_h)
                
                filename=dir_output+"pano"+"V"+str(index_v)+"H"+str(index_h)+".jpg"
                # take a picture on each step
                #self.triggerCam(filename)
                
                #print("\n"+filename)
                #print("\n Position Vertical : %f \t Horizontal : %f"%(pos_v,pos_h))


    def triggerCam(self,filename):
        # Triggers the Cam using the cmd-tool of gphoto2 and download+save the picture in 'filename'
        print("\n click")

        cmd="gphoto2 --capture-image-and-download --keep --filename "+filename+" "
		
        try:
            os.popen(cmd)
        except:
            stderr.write("\nERROR @triggerCam by calling %s"%cmd)
            stderr.write("\nMake sure that gphoto2 is correct installed and the camera is connected in normal Mode")
        exit()

