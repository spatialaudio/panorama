from sys import stderr
import configparser
import argparse
from python_core_components.ptfile_creator import PtCreator
from python_core_components.varisphear import VariSphear


def arg_options():

    # init options
    parser = argparse.ArgumentParser(
        description='''Create the PTSticher-Input File ''')

    parser.add_argument(
        '--aperature',
        type=int,
        nargs=1,
        dest='aperature',
        default=None,
        metavar=('APERATURE ANGLE'),
        help='''Set the aperature angle for PTSticher.
            Unlike ANGLE_H and ANGLE_V this value have to be
            the exact apterature angle of your camera ( no overlap ).
            This value will be saved in "panorama.cfg"
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
        '-n',
        '--noFile',
        dest='noFile',
        action='store_true',
        help='Skip the step of generate PtFile')

    parser.add_argument(
        '--ptfile',
        dest='ptfile',
        default=None,
        metavar=('PTFILE'),
        help='''Specifies the filename of the ptfile.
        ( default: pt_file.txt ) ''')

    # return arguments
    return parser.parse_args()


def main():

    # get arguments
    args = arg_options()

    # set path to panorama.cfg
    path_cfg = args.config
    if(not path_cfg):
        path_cfg = 'panorama.cfg'

    # get filename of PtFile
    pt_filename = args.ptfile
    if(not pt_filename):
        pt_filename = 'pt_file.txt'

    # get values from 'path_cfg'
    config = configparser.ConfigParser()
    try:
        config.read(path_cfg)
        test = config['camera']['vertical_angle']
    except:
        stderr.write("\n ERROR: Can´t open file: %s !\n exit \n" % path_cfg)
        exit()

    # set new values
    if(args.aperature):
        config['camera']['pure_aperature'] = str(args.aperature[0])
    if(args.directory):
        config['output']['directory'] = args.directory
    if(args.abc):
        config['camera']['param_a'] = str(args.abc[0])
        config['camera']['param_b'] = str(args.abc[1])
        config['camera']['param_c'] = str(args.abc[2])

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
    aperature = float(config['camera']['pure_aperature'])
    param_a = float(config['camera']['param_a'])
    param_b = float(config['camera']['param_b'])
    param_c = float(config['camera']['param_c'])

    dir_output = config['output']['directory']

    # Get Interfaces / Ports to VariSphear
    port_top = config['varisphear']['serialport_top']
    port_base = config['varisphear']['serialport_base']

    variSphear = VariSphear(port_top, port_base)

    # Mapping of angles to Motorpositions
    li_motorTop = variSphear.map_motor_top(angle_v)
    li_motorBase = variSphear.map_motor_base(angle_h)

    # Create PTSticher-File
    pt_creator = PtCreator(dir_output, param_a, param_b, param_c)
    output = pt_creator.create_file(li_motorTop, li_motorBase, aperature)

    # Save

    if(not args.noFile):
        with open(pt_filename, 'w') as ptfile:
            ptfile.write(output)
            print(' File ' + pt_filename + ' generated')

if __name__ == '__main__':

    main()
