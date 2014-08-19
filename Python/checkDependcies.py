#import schunk
#import serial
import argparse
import sys
import os

def arg_options():

    #init options
    parser = argparse.ArgumentParser(description='A simple program which checks if all software requirements are fulfilled. ' )
    
    
    parser.add_argument('--config', dest='config',default=None,metavar=('CONFIGFILENAME'),
                   help='Create a configfile with the given name and fill it with default values.')

    # return arguments
    return parser.parse_args()




def main():
    
    # get arguments
    args = arg_options()

    if(args.config):
        try:
            from pythonPanorama.configCreater import configCreater
            print("create configfile")
            config=configCreater()
            config.createConfigfile(args.config)        
        except:
            print("\n You need to install setup-tools first !")
        exit()

    print(" Start check \n")
        
    print(" Your version of python should be > version 2.7 ")
    print(" Your version : "+sys.version )           
    
    try:
        import configparser
        test=True
    except:
        test=False

    print("\n Check if setup-tools are installed : "+str(test))

    print("\n Check if gphoto2 is installed [@ /usr/bin/gphoto2 ] :  "+str(os.path.isfile('/usr/bin/gphoto2')))

    print("\n Check if hugin is installed [@ /usr/bin/hugin ]: "+str(os.path.isfile('/usr/bin/hugin')))

    print("\n Check if enblend is installed [@ /usr/bin/enblend ]: "+str(os.path.isfile('/usr/bin/enblend')))

    try:
        import schunk
        test=True
    except:
        test=False

    print("\n Check if the schunk-modul is installed : "+str(test))

    # other checks will follow

if __name__ == '__main__':
        
    main()    




