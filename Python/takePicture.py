# -*- coding: utf-8 -*-
from sys import stderr
import configparser
import argparse
from python_core_components.panorama_calculation import PanoramaCalculator
from python_core_components.varisphear import VariSphear


def arg_options():

    # init options
    parser = argparse.ArgumentParser(
        description='''Calculate the motorpositions of the VariSphear
            depending on the aperature angles of the camera
            and take pictures.
            Final this pictures will be saved in the output directory
            spezifed in "panorama.cfg". ''')

    parser.add_argument(
        '--angle',
        type=int,
        nargs=2,
        dest='angle',
        default=None,
        metavar=('VERTICAL', 'HORIZONTAL'),
        help='''Set the vertical aperature angle
            and the horizontal aperature angle for calculations.
            This values will be saved in "panorama.cfg"
            unless "-t" is set.
            ( default: values will be read from "panorama.cfg instead" )''')

    parser.add_argument(
        '--directory',
        dest='directory',
        default=None,
        metavar=('DIRECTORY'),
        help='''Set the realtive path to your output directory.
            This value will be saved in "panorama.cfg" unless "-t" is set.
            ( default: path will be read from "panorama.cfg instead " ) ''')

    parser.add_argument(
        '--config',
        dest='config',
        default=None,
        metavar=('CONFIGFILE'),
        help='''Specifies the realtive path to "panorama.cfg"
        ( default: panorama.cfg ) ''')

    parser.add_argument(
        '-t',
        '--tmp',
        dest='tmp',
        action='store_true',
        help='Prevent any changes of "panorama.cfg" done by this program ')

    parser.add_argument(
        '-i',
        '--info',
        dest='info',
        action='store_true',
        help='Show info before mesurement starts')

    parser.add_argument(
        '-n',
        '--noPicture',
        dest='noPicture',
        action='store_true',
        help='Skip the step of driving to each position and taking pictures')

    # return arguments
    return parser.parse_args()


def main():

    # get arguments
    args = arg_options()

    # set path to panorama.cfg
    path_cfg = args.config
    if(not path_cfg):
        path_cfg = 'panorama.cfg'

    # get values from 'path_cfg'
    config = configparser.ConfigParser()
    try:
        config.read(path_cfg)
        test = config['camera']['vertical_angle']
    except:
        stderr.write("\n ERROR: Can´t open file: %s !\n exit \n" % path_cfg)
        exit()

    # set new values
    if(args.angle):
        config['camera']['vertical_angle'] = str(args.angle[0])
        config['camera']['horizontal_angle'] = str(args.angle[1])
    if(args.directory):
        config['output']['directory'] = args.directory

    # save new values in 'panorama.cfg' if not permitted
    if(not args.tmp):
        try:
            with open(path_cfg, "w") as configfile:
                config.write(configfile)
        except:
            stderr.write("\n ERROR: Can´t open file %s !\n exit \n" % path_cfg)
            exit()

    angle_h = float(config['camera']['horizontal_angle'])
    angle_v = float(config['camera']['vertical_angle'])
    dir_output = config['output']['directory']

    calc = PanoramaCalculator()
    variSphear = VariSphear()

    if(args.info):
        calc.show_info()

    calc.show_statistic(angle_v, angle_h, dir_output)
    # Mapping of angles to Motorpositions
    li_motorTop = variSphear.map_motor_top(angle_v)
    li_motorBase = variSphear.map_motor_base(angle_h)

    # Taking the Pictures
    if(not args.noPicture):
        variSphear.taking_pictures(
            li_motorTop, li_motorBase, dir_output, path_cfg)

if __name__ == '__main__':

    main()
