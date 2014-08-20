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
                        
    
    1) : Connect the VariSphear with your PC and make sure that both are in the same subnetwork.
         Try to ping the VariSphear to check if your connection is correct.
         No connection --> check your static IP-Adress and make sure the VariSphear is on.

    2) : Check if your driver is already up --> type : ps ax | grep npreal  
         driver is not up --> type : sudo /usr/lib/npreal2/driver/mxloadsrv

    3) : Connect your camera with your PC via USB.
         Make sure your camera is in "normal Mode" and powered on.
         Check if your PC recognised your camera by typing : gphoto2 --auto-detect
         Check if your Cam is supported by gPhoto2 by typing : gphoto2 --capture-image-and-download --keep
         ( This cmd is used by varisphear.py to take pictures. If it doesn´t work, look at "gphoto2 --help" for alternativ Instructions. )
         
    4) : Remember to activate your virtual enviroment ( if you installed one )
         --- Example :
            - We activate our virtual python enviroment "env_panorama"
            > source /env_panorama/bin/activate


    5) : Create a config-file or copy/edit the already existed one.
         Your configfile contains all your camera specific parameter and your output-directory.

         Creating a new one can easily be done by typing "python3 checkDependcies.py --configfile myConfig.cfg"
         If there are more than one config-file, make sure your program used the correct one by specifing the path.
         In our Example we use our programs for editing the configfile.

         --- Example :
            - We create a configfile "panoExample.cfg"
            > python3 checkDependcies.py --config myConfig.cfg 

         
    6) : Calculating the nodalpoint.
         This avoid parallax , very importent etc. pp. 
         Follow the instructions ( Hannes ?! ).

         --- Example :
             -
             >
             -
                           

    7) : Taking pictures.
         Now we have to take a lot of pictures.
         Later on we will stich this pictures together to our room-panorama.
          
         For taking this pictures we used the programm "takePicture.py".
         Please make sure that the VariSphear and your camera is correct connect to your PC.  
         Have a look at our Example to see how it is done.
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


    8) : Improve picture.
         Before we get to the stiching, we have to clean our picture from radial disortions.
         For this purpose we use "improvePicture.py". 
         Type : 
            python3 improvePicture.py -h
         for further information

         --- Example :
            - We added our disortion parameter we get in step 0) to "myConfig.cfg" using "improvePicture.py"
            > python3 improvePicture.py --abc 0.0001 0.0002 0.0003 --config myConfig.cfg -n
            - We start improving of all pics in folder "RoomPics"
            > python3 improvePicture.py --config myConfig.cfg
            - Take a look at "RoomPics", all corrected pictures have the suffix "_corr".
            - The next programm "stichPicture.py" stich only pictures with this suffix.   
        
    9) : Stich picture together.
         Type:
            python3 stichPicture.py -h
         for further information. 
         --- Example :
               
            
