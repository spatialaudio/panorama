# -*- coding: utf-8 -*-
#import schunk
#import serial
import math


# "top" indicate the motor, which is responsible for the vertical rotation   
#top = schunk.Module(schunk.SerialConnection(
#    0x0B, serial.Serial, port='COM2', baudrate=9600, timeout=None))
#if(not top.toggle_impulse_message()):
#    top.toggle_impulse_message();


# "base" indicate the motor, which is responsible for the horizontal rotation   
#base = schunk.Module(schunk.SerialConnection(
#    0x0B, serial.Serial, port='COM1', baudrate=9600, timeout=None))
#if(not base.toggle_impulse_message()):
#    base.toggle_impulse_message();    
    
#top.move_pos_blocking(0)
#base.move_pos(0)
#base.move_pos_blocking(0)        
        
def calcNumStages(angle_v):
    # How many horizontal Rotations do we need ?
    # We have to cover min. 180° vertical 
    max_angle=180.0;

    try:
        NumStages=int(math.ceil(max_angle/angle_v));
    except:
        print("\nERROR @calcNumStages : invalid vertical angle");
        exit();

    return NumStages

def calcStepsRotation(angle_h):
    # In how many steps is each horizontal Rotation done ?
    # We have to cover min. 360° horizontal
    # One each step we are taking a picture
    max_angle=360.0;
    try:
        RotationSteps=int(math.ceil(max_angle/angle_h));
    except:
        print("\nERROR @calcStepsRotation : invalid horizontal angle");
        exit();


    return RotationSteps



def mapMotorTop(angle_v):
    # Creates a List containing the motorposition for each vertical stage.
    # 
    
    # Number of vertical Stages
    NumStages=int(calcNumStages(angle_v));

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

def mapMotorBase(angle_h):
    # Creates a List containing the motorposition for each horizontal step/picture .
    # 
    
    # start Position is at 0°
    start=0;
    
    # Number of Steps per Rotation
    RotationSteps=int(calcStepsRotation(angle_h));    
    
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


def takingPictures(li_motorTop,li_motorBase):
    # drive to all motorposition and trigger cam !
    
    for pos_v in li_motorTop:
            
        for pos_h in li_motorBase:
    
            print("\n Position Vertical : %f \t Horizontal : %f"%(pos_v,pos_h));

def triggerCam():
    
    print("\n Trigger Cam ");


def showInfo():
    print("\n °----------------------------------------°");
    print("\n Info:");
    print("\n If you to increase the overlap between adjacent pictures, you should pass a smaller aperture angle.");
    print("\n The Number of needed picture is always rounded up.");
    print("\n Note to the progress of taking picture:");
    print("\n There are x vertical stages ( depending on the vertical aperature angle ).");
    print("\n We start with the top stage");
    print("\n Each vertical stage consist of one horizontal Rotation ( == 360° ).");
    print("\n Each horizontal Rotation consist of y steps ( depending on horizontal aperature angle ).");
    print("\n In each step we take one picture.");    
    print("\n °----------------------------------------°");

def showStatistic(angle_v,angle_h):
    print("\n °----------------------------------------°");
    print("\n Statistic:");
    print("\n Vertical aperture angle: %d°"%angle_v);
    print("\n\t Number of Stages: %d"%calcNumStages(angle_v));
    print("\n Horizontal aperture angle: %d°"%angle_h);
    print("\n\t Number of steps: %d"%calcStepsRotation(angle_h));
    sumPictures=calcStepsRotation(angle_h) * calcNumStages(angle_v);
    print("\n Sum of picture to be make: %d"%(sumPictures));
    print("\n °----------------------------------------°");
    

    
        
    

# Get vertical aperture angle
angle_v=float(input("\n Insert vertical aperture angle of Cam [degree] : \n  "));
# Get horizontal aperture angle
angle_h=float(input("\n Insert horizontal aperture angle of Cam [degree] : \n  "));

showInfo();
print("\n");
showStatistic(angle_v,angle_h);

# Mapping of angles to Motorpositions
li_motorTop=mapMotorTop(angle_v);
li_motorBase=mapMotorBase(angle_h);


print("\n Motor Vertikal"+str(li_motorTop));
print("\n Motor Horizontal"+str(li_motorBase));

# Taking the Pictures
takingPictures(li_motorTop,li_motorBase)


