# -*- coding: utf-8 -*-
from sys import stderr
import configparser
import argparse
from python_core_components.panorama_calculation import PanoramaCalculator
from python_core_components.improver import PicImprover


def arg_options():
    ''' init options '''

    parser = argparse.ArgumentParser(
        description='''Load all pictures from the directory spezifed in "panorama.cfg"
                    and improve them by removing radial disortions
                    and correcting chromatic aberrations.
                    For this purpose we use fulla ( a subprogram of hugin ).
                    The quality of improvement depends on the quality of
                    mesaured lens correction parameters a, b and c.''')

    parser.add_argument(
        '--directory',
        dest='directory',
        default=None,
        metavar=('DIRECTORY'),
        help='''Set the realtive path to directory.
            This value will be saved in "panorama.cfg"
            unless "-t" is set.
            ( default: path will be read from "panorama.cfg" instead )
            ''')

    parser.add_argument(
        '--config',
        dest='config',
        default=None,
        metavar=('CONFIGFILE'),
        help='''Specifies the realtive path to "panorama.cfg"
            ( default: panorama.cfg ) ''')

    parser.add_argument(
        '--fulla',
        dest='fulla',
        default=None,
        metavar=('FULLA'),
        help='''Specifies the realitive path to fulla
            ( default: path will be read from "panorama.cfg instead " )
            ''')

    parser.add_argument(
        '--abc',
        type=float,
        nargs=3,
        dest='abc',
        default=None,
        metavar=('A', 'B', 'C'),
        help='''Set the lens correction parameters a, b and c for the improvement.
            This values will be saved in "panorama.cfg" unless "-t" is set.
            ( default: values will be read from "panorama.cfg instead" )
            ''')

    parser.add_argument(
        '-t',
        '--tmp',
        dest='tmp',
        action='store_true',
        help='Prevent any changes of "panorama.cfg" done by this program ')

    parser.add_argument(
        '-n',
        '--noImprovement',
        dest='noImprovement',
        action='store_true',
        help='Skip the step of improving pictures')

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
    if(args.abc):
        config['camera']['param_a'] = str(args.abc[0])
        config['camera']['param_b'] = str(args.abc[1])
        config['camera']['param_c'] = str(args.abc[2])
    if(args.fulla):
        config['hugin']['fulla'] = args.fulla

    if(args.directory):
        config['output']['directory'] = args.directory

    # save new values in 'panorama.cfg' if permitted
    if(not args.tmp):
        try:
            with open(path_cfg, "w") as configfile:
                config.write(configfile)
        except:
            stderr.write("\n ERROR: Can´t open file %s !\n exit \n" % path_cfg)
            exit()

    param_a = float(config['camera']['param_a'])
    param_b = float(config['camera']['param_b'])
    param_c = float(config['camera']['param_c'])
    fulla = config['hugin']['fulla']
    dir_output = config['output']['directory']

    improve = PicImprover(dir_output, fulla)

    improve.show_statistic(param_a, param_b, param_c)

    if(not args.noImprovement):
        improve.improve_pic(param_a, param_b, param_c)

if __name__ == '__main__':

    main()
