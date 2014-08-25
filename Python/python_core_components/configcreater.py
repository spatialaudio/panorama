from sys import stderr
import configparser


class ConfigCreater:
    ''' Generate a config-file '''
    def __init__(self):
        pass

    def create_configfile(self, filename):
        config = configparser.ConfigParser()

        # section : output
        config['output'] = {}
        config['output']['directory'] = 'myOutputFolder'

        # section : 'camera'
        config['camera'] = {}
        config['camera']['vertical_angle'] = '60'
        config['camera']['horizontal_angle'] = '90'
        config['camera']['param_a'] = '0.000123'
        config['camera']['param_b'] = '0.000123'
        config['camera']['param_c'] = '0.000123'

        # section : hugin
        config['hugin'] = {}
        config['hugin']['fulla'] = '/usr/bin/fulla'
        config['hugin']['enblend'] = '/usr/bin/enblend'

        # section : varisphear
        config['varisphear'] = {}
        config['varisphear']['serialport_top'] = '/dev/ttyr01'
        config['varisphear']['serialport_base'] = '/dev/ttyr00'

        with open(filename, 'w') as configfile:
            config.write(configfile)
