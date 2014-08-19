# -*- coding: utf-8 -*-
import schunk
import serial
import argparse
from sys import stderr

def arg_options():

    #init options
    parser = argparse.ArgumentParser(description='A simple programm for moving the varisphear by using cmd-line. It support you by determine the nodalpoint ' )
    
    
    parser.add_argument('-l',type=float, nargs=1,dest='left',default=None, metavar=('DEGREE'), 
                   help='Rotate DEGREE steps anticlockwise ')

    parser.add_argument('-r',type=float, nargs=1,dest='right',default=None, metavar=('DEGREE'), 
                   help='Rotate DEGREE steps clockwise ')


    parser.add_argument('--down',dest='down',action='store_true',help='Drive the top.modul to the -90 degree position')

    parser.add_argument('--up',dest='up',action='store_true',help='Drive the top.modul to the 0 degree position')

    parser.add_argument('--init',dest='init',action='store_true',help='Drive both moduls to the 0 degree position ')

    # return arguments
    return parser.parse_args()




def main():
    
    # get arguments
    args = arg_options()

    top = schunk.Module(schunk.SerialConnection( 0x0B, serial.Serial, port='COM2',baudrate=9600, timeout=None))
    if(not top.toggle_impulse_message()):
        top.toggle_impulse_message();


    # Init motor
    try:
    # "top" indicate the motor, which is responsible for the vertical rotation   
        top = schunk.Module(schunk.SerialConnection( 0x0B, serial.Serial, port='COM2',baudrate=9600, timeout=None))

        if(not top.toggle_impulse_message()):
            top.toggle_impulse_message();
    except:
        stderr.write("\nERROR @takingPicture by connecting to top schunkModul")
        exit()
    
    try:
    # "base" indicate the motor, which is responsible for the horizontal rotation   
        base = schunk.Module(schunk.SerialConnection(0x0B, serial.Serial, port='COM1',baudrate=9600, timeout=None))

        if(not base.toggle_impulse_message()):
            base.toggle_impulse_message();  
    except:
        stderr.write("\nERROR @takingPicture by connecting to base schunkModul")
        exit()

    

    if(args.left):
        print("left: "+str(args.left[0]%360.0))
        top.move_pos_rel_blocking(args.left[0]%360.0)
    elif(args.right):
        print("right: "+str(args.right[0]%360.0))
        top.move_pos_rel_blocking(args.right[0]%360.0)
    
    if(args.init):
        print("init")
        top.move_pos_blocking(0)
        base.move_pos_blocking(0)
    elif(args.up):
        print("up")
        top.move_pos_blocking(0)
    elif(args.down):
        print("down")
        top.move_pos_blocking(-90)
    
        

if __name__ == '__main__':
        
    main()    




