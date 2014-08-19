# -*- coding: utf-8 -*-
from sys import stderr
import configparser
import argparse
from pythonPanorama.PicSticher import picSticher
from pythonPanorama.panoramaCalculation import panoramaCalculation

def arg_options():

    #init options
    parser = argparse.ArgumentParser(description='Load all corrected pictures ( pictures with suffix "_corr.JPG" ) from given directory and stich them together. For this purpose enblend is used , which will be installed with hugins. Type %prog -i to watch the requirments' )
    
    parser.add_argument('--directory', dest='directory',default=None,metavar=('DIRECTORY'),
                   help='Set the realtive path to your output directory. This value will be saved in "panorama.cfg" unless "-t" is set. ( default: path will be read from "panorama.cfg instead " ) ')

    parser.add_argument('--config', dest='config',default=None,metavar=('CONFIGFILE'),
                   help='Specifies the realtive path to "panorama.cfg" ( default: panorama.cfg ) ')

    parser.add_argument('--enblend', dest='enblend',default=None,metavar=('ENBLEND'),
                   help='Specifies the realitive path to enblend ( default: path will be read from "panorama.cfg instead " ) ')
    
    parser.add_argument('--stages',type=int, nargs=1,dest='stages',default=None, metavar=('STAGES'), 
                   help='Specifies the number of vertical stages.  ( default: values will be read from "panorama.cfg instead" )')

    parser.add_argument('-o','--orginal',dest='orginal',action='store_true',help='Load all orginal picture instead of the corrected ones')

    parser.add_argument('-t','--tmp',dest='tmp',action='store_true',help='Prevent any changes of "panorama.cfg" done by this program ')

    parser.add_argument('-n','--noStiching',dest='noStich',action='store_true',help='Skip the step of stiching pictures')

    parser.add_argument('-i','--info',dest='info',action='store_true',help='Show info before mesurement starts')

    
    # return arguments
    return parser.parse_args()




def main():
    
    # get arguments
    args = arg_options()
    
    # set path to panorama.cfg
    path_cfg=args.config
    if(not path_cfg):
        path_cfg='panorama.cfg';


    # get values from 'path_cfg'    
    config = configparser.ConfigParser()
    try:
        config.read(path_cfg)
        test=config['camera']['vertical_angle']
    except:
            stderr.write("\n ERROR: Can´t open file: %s !\n exit \n"%path_cfg)
            exit()
        
    # set new values
    if(args.enblend):
        config['hugin']['enblend']=args.enblend
    if(args.directory):
        config['output']['directory']=args.directory


    # save new values in 'panorama.cfg' if permitted
    if(not args.tmp):
        try: 
            with open(path_cfg,"w") as configfile:
                config.write(configfile)
        except:
            stderr.write("\n ERROR: Can´t open file %s !\n exit \n"%path_cfg)
            exit()                
    
    # short vars for work
    enblend=config['hugin']['enblend']
    dir_output=config['output']['directory']
    
    # instance of picSticher 
    sticher=picSticher(dir_output,enblend)

    
    if(args.info):
        sticher.showInfo()
    
    # set stages
    if(args.stages):
        stages=args.stages[0]
    else:
        calc=panoramaCalculation()
        stages=int(calc.calcNumStages(config['camera']['vertical_angle']))        

    # create a dictonary, which contains a list of a all vertical pictures for a given horizontal step
    dict_picture=sticher.splitPics(args.orginal,stages)

    # show some statistics
    sticher.showStatistic(dict_picture)

    # stiching the Pictures
    if(not args.noStich):
        sticher.stichPictures(dict_picture)

if __name__ == '__main__':
        
    main()    




