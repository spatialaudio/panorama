# -*- coding: utf-8 -*-
import math
from sys import stderr


class PanoramaCalculator:
    ''' Calculate Rotationsteps and Number of vertical Stages
        depending on given aperature angles.'''

    def __init__(self):
        pass

    def calc_num_stages(self, angle_v):
        # How many horizontal Rotations do we need ?
        # We have to cover min. 180° vertical
        max_angle = 180.0

        try:
            NumStages = int(math.ceil(max_angle / float(angle_v)))
        except:
            stderr.write("\nERROR @calcNumStages : invalid vertical angle")
            exit()

        return NumStages

    def calc_steps_rotation(self, angle_h):
        # In how many steps is each horizontal Rotation done ?
        # We have to cover min. 360° horizontal
        # One each step we are taking a picture
        max_angle = 360.0
        try:
            RotationSteps = int(math.ceil(max_angle / float(angle_h)))
        except:
            stderr.write(
                "\nERROR @calcStepsRotation : invalid horizontal angle")
            exit()

        return RotationSteps

    def show_info(self):
        print("\n °----------------------------------------°")
        print("\n Info:")
        print(
            '''\n If you to increase the overlap between adjacent pictures,
            you should pass a smaller aperture angle.''')
        print("\n The Number of needed picture is always rounded up.")
        print("\n Note to the progress of taking picture:")
        print(
            '''\n There are x vertical stages
            ( depending on the vertical aperature angle ).''')
        print("\n We start with the top stage")
        print(
            '''\n Each vertical stage consist of
            one horizontal Rotation ( == 360° ).''')
        print(
            '''\n Each horizontal Rotation consist of y steps
            ( depending on horizontal aperature angle ).''')
        print("\n In each step we take one picture.")
        print("\n °----------------------------------------°")

    def show_statistic(self, angle_v, angle_h, output):
        print("\n °----------------------------------------°")
        print("\n Statistic:")
        print("\n Vertical aperture angle: %d°" % angle_v)
        print("\n\t Number of Stages: %d" % self.calc_num_stages(angle_v))
        print("\n Horizontal aperture angle: %d°" % angle_h)
        print("\n\t Number of steps: %d" % self.calc_steps_rotation(angle_h))
        sumPictures = self.calc_steps_rotation(
            angle_h) * self.calc_num_stages(angle_v)
        print("\n Sum of picture to be make: %d" % (sumPictures))
        print("\n Picture will be saved in: %s" % (output))
        print("\n °----------------------------------------°")
