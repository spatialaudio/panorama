PROJECT PANORAMA

Tutorial:
    We will build a tutorial where we will guide you to your first 3D-Panorama to get familiar with our programs.
    The location of this tutorial is @ https://github.com/spatialaudio/panorama-examples.
    For this purpose you don´t need to communicate with the varisphear because the picture are already made.

Software dependencies:

    The following instructions are tested for Ubuntu (3.11.0-12-generic) and Debian.
    Please refer the README of each software package for your specific install instructions.         
    
-- Setup Python:
        
    0) [ optional ] : We recommend the use of a virtual environment for our python project.
                      This prevent namespace error etc.
                      It is easily set up with "virutalenv" :
                                sudo apt-get install virtualenv
                                virtualenv --python=python3 MyNewVirtualEnv

                      To activate this environment you simple type:
                                source MyNewVirtualEnv/bin/activate
                      All python-moduls you installed in this environment, exists only in this environment.
                      Remember : Before starting work you have to activate your virtual environment !
                      Take a look @ http://docs.python-guide.org/en/latest/dev/virtualenvs/ for further information !

    1) : Install python3:
            run:
                sudo apt-get install python3

    2) : Install pip and the setup-tools:
            Browse to: https://pip.pypa.io/en/latest/installing.html
            download "get-pip.py"
            run:
                python3 get-pip.py

    3) : Install schunk :
            pip3 install --user SchunkMotionProtocol
            ( Mehr Infos @ https://pypi.python.org/pypi/SchunkMotionProtocol/0.2.0 )
    
    4) : Install seriell :
            pip3 install pyserial
            ( Mehr Infos @ http://pythonhosted.org//pyserial/pyserial.html#installation )


-- Setup gPhoto2:  
   
    We use gphoto2 to communicate with our camera    

    1) : Install libtool :

            Browse to: https://www.gnu.org/software/libtool/
            download "libtool-2.4.2.tar.gz"
            Extract and change to extracted Direction.
			run ( as root ) :
			    ./configure --prefix=/usr
			    make 
                make install           
    2) : Install libgphoto2 :

            Browse to: http://www.gphoto.org/
            download "libgphoto2".
            Extract and change to extracted Direction.
            run ( as root ):            
      	    	./configure --prefix=/usr/local            
	           	make
		        make install

    3) : Install gphoto2 :

            Browse to: http://www.gphoto.org/
            download "gphoto2"
            Extract and change to extracted Direction.
            run ( as root ):            
                apt-get install libpopt-dev
                apt-get install libaa1-dev
                ./configure
                make
                make install

            
-- Setup Hugin:
    
    We use hugin and enblend for stitching and improving our pictures.

    0) [ optional ] :  For reading the install-instructions for your system
                       browse to: http://hugin.sourceforge.net/download/
 
    1) : Add to Repository :
               
            run :
                ( if "add-apt-repsitory" cause a "cmd not found" you have to install it with :
                     sudo apt-get install software-properties-common
                )
                sudo add-apt-repository ppa:hugin/hugin-builds

    2) : Install Hugin :

            run :
		        sudo apt-get update
                sudo apt-get install hugin enblend

-- Setup Varisphear-Driver

    0) : For communication with the VariSphear the Host-PC need a static IP-adress in the same Sub-Network.


    1) : Install Linux Headers :

            run ( as root ):
                apt-get upgrade
                apt-get install linux-headers-$(uname -r)

    2) : Install Driver :

            Ask : support@moxa.com
            download "npreal2xx.tgz".
            Extract and change to extracted Direction.
            Check if you fullfill all requirments mentioned in npreal2xx/README ( section 3 )             
            run ( as root ):
                ./mxinst

    3) : Map tty-Ports :

            Change to /usr/lib/npreal2/driver
            run ( as root ):
                ./mxaddsvr 139.6.16.253 4
                                
             
            npreald2.cf should look like :
                ....stuff...
                0	139.6.16.253	950	966	1	0	ttyr00	cur00	0	0	
                1	139.6.16.253	951	967	1	0	ttyr01	cur01	0	0	
                2	139.6.16.253	952	968	1	0	ttyr02	cur02	0	0	
                3	139.6.16.253	953	969	1	0	ttyr03	cur03	0	0
            
            to load these moduls run ( as root ):
                ./mxloadsrv    
            
            In directory /dev should now ttyr00, ttyr01, ttyr02, ttyr03 exist.
            In our case we use ttyr00 ( baseMotor ) and ttyr01 ( topMotor ).
            If you want to chance this you have to it by manuelly edit the config File.
            We created a config File in Step 6 in "Getting Started". 

            For further instructions have a look at npreal2xx/README !

    4) : [ optional ] :
            
            start driver after boot ? --> run :
                update-rc.d npreals defaults
                
            test if driver is up --> run :
                ps ax | grep npreal    


------------°

-- Getting started :

    I already mentioned the tutorial , didn´t I ?
    
    0) : Determine the disortion-parameter (a,b,c,d) of your camera. ( Alaa ?! ).
         --- Example :   
         
    1) : We configured our camera. Please refer to the manual of your camera for special instructions.
         We use a Canon "EOS-20D" and make the following settings :
            - quality of picture == high
            - autofocus off
            - shortest focal length ( == max. aperature angle )
            - set a fix white balance ( it depends on your room, so take a few picture to figured out a good value )
            - image stabilizer off
            - set a fix ISO-Value and a fix aperture-setting ( we choose 11 )
            - optional : high exposure time
         The optimal setting depends on the room.
         Take a few picture with variation in ISO, exposure time and aperture-setting to determine your settings.     
    
    2) : Connect the VariSphear with your PC and make sure that both are in the same subnetwork.
         Try to ping the VariSphear to check if your connection is correct.
         No connection --> check your static IP-Adress and make sure the VariSphear is on.

    3) : Check if your driver is already up --> type : ps ax | grep npreal  
         driver is not up --> type : sudo /usr/lib/npreal2/driver/mxloadsrv

    4) : Connect your camera with your PC via USB.
         Make sure your camera is in "normal Mode" and powered on.
         Check if your PC recognised your camera by typing : gphoto2 --auto-detect
         Check if your Cam is supported by gPhoto2 by typing : gphoto2 --capture-image-and-download --keep
         If the error 'Could not claim the USB device' occurs , type : ps ax | grep gphoto and kill all of this prozesses
         ( This cmd is used by varisphear.py to take pictures. If it doesn´t work, look at "gphoto2 --help" for alternativ Instructions. )
         
    5) : Remember to activate your virtual enviroment ( if you installed one )
         --- Example :
            - We activate our virtual python enviroment "env_panorama"
            > source /env_panorama/bin/activate


    6) : Create a config-file or copy/edit the already existed one.
         Your configfile contains all your camera specific parameter and your output-directory.

         Creating a new one can easily be done by typing "python3 checkDependcies.py --configfile myConfig.cfg"
         If there are more than one config-file, make sure your program used the correct one by specifing the path.
         In our Example we use our programs for editing the configfile.

         --- Example :
            - We create a configfile "panoExample.cfg"
            > python3 checkDependcies.py --config myConfig.cfg 

         
    7) : Calculating the nodalpoint.
         This avoid parallax , very importent etc. pp. 
         Follow the instructions ( Hannes ?! ) (Yeah Moritz?).
         Use "nodalpointHelper.py"
		 
		 "A picture is worth a thousand words"
		 
		 To get an idea of what you have to do here please check the wiki.
		 (https://github.com/spatialaudio/panorama/wiki/(Guide)-No-Parallax-Point)
		 You will find a detailed guide that even contains lots of pictures
		 to make this process as understandable as possible.

         --- Example :
             -
             >
             -
                           

    8) : Taking pictures.
         Now we have to take a lot of pictures.
         Later on we will stich this pictures together to our room-panorama.
          
         For taking this pictures we used the programm "takePicture.py".
         Please make sure that the VariSphear and your camera is correct connect to your PC.  
         Have a look at our Example to see how it is done.
         You can use "nodalpointHelper.py" to determine your aperature angle.
         Make sure that there is enough covering between two neighboring pictures ( ~ 20 % ).

         Type : > python3  takePicture.py -h 
         for further information.          

         --- Example :
            - We create an output folder "RoomPics" for the output pictures
            > mkdir RoomPics
            - We added our output folder to our configfile "myConfig.cfg" using "takePicture.py"
            > python3 takePicture.py --directory RoomPics --config myConfig.cfg -n
            - We added our aperature angles ( vertical=60 , horizontal=100 ) to our configfile "myConfig.cfg"
            > python3 takePicture.py --angle 60 100 --config myConfig.cfg -n
            - We start the routine
            > python3 takePicture.py --config myConfig.cfg


    9) : Create PtSticher-File
         Before we get to the stiching, we have to build a PtSticher-File with all the externel parameter. 

         Type : 
            python3 createPtFile.py -h
         for further information

         --- Example :
            - We added the exact aperature angle of our camera to "myConfig.cfg" using "createPtFile.py"
            > python3 createPtFile.py --config myConfig.cfg --aperature 66 -n          
            - We added our disortion parameter we get in step 0) to "myConfig.cfg" using "createPtFile.py"
            > python3 createPtFile.py --abc 0.0001 0.0002 0.0003 --config myConfig.cfg -n
            - We added the location of Hugin in our Windows OS ( in this Version we only support .bat files )
            > python3 createPtFile.py --hugin e:\Hugin --config myConfig.cfg -n
            - We generate our PtSticher-File and our Bat-File in our Output Folder
            > python3 createPtFile.py --config myConfig.cfg
  
        
    10) : Stich picture together.
          We copy our whole output Folder to our Windows OS.
          Now you can stich all puctures together using our generated Bat-Files.
		  
		  hugin_scripted.bat 			for Method 1 (finding control points)
		  hugin_hugin_ptstitcher.bat	for Method 2 (camera paramter [needs PtStichter file of step 9])
		  hguin_template				for Method 3 (see 10b))	
			
	10b): If you want to make use of a template create a folder named "temp" in the folder that contains
		  the hugin_template.bat script. Place your *.pto file in that temp folder and run the script.
		  
		  If you have chosen to assemble the panorama by hugin (controlpoints) you can find the *.pto file
		  of your project in the generated temp folder for later use.
            
