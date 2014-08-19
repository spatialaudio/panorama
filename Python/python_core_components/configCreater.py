# -*- coding: utf-8 -*-
from sys import stderr
import configparser


class configCreater:
    
    def __init__(self):
        pass

    def createConfigfile(self,filename):
        config = configparser.ConfigParser()
        
        # section : output
        config['output']={}
        config['output']['directory']='myOutputFolder'

        # section : 'camera'
        config['camera']={}
        config['camera']['vertical_angle']='60'
        config['camera']['horizontal_angle']='90'
        config['camera']['param_a']='0.000123'
        config['camera']['param_b']='0.000123'
        config['camera']['param_c']='0.000123'
                  
        # section : hugin
        config['hugin']={}  
        config['hugin']['fulla']='/usr/bin/fulla' 
        config['hugin']['enblend']='/usr/bin/enblend'  


        # section : varisphear
        config['varisphear']={}
        config['varisphear']['serialport_top']='COM2'
        config['varisphear']['serialport_base']='COM1'

        with open(filename, 'w') as configfile:
            config.write(configfile)

