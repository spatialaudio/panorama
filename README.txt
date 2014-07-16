PROJECT PANORAMA

Tutorial:
    We will build a tutorial where we will guide you to your first 3D-Panorama to get familiar with our programs.
    The location of this tutorial is @ https://github.com/spatialaudio/panorama-examples.
    For this purpose you don´t need to communicate with the varisphear because the picture are already made.

Software dependencies:

    1) [ optional ] : We recommend the use of a virtual environment for our python project.
                      This prevent namespace error etc.
                      It is easily set up with "virutalenv" :
                                sudo apt-get install virtualenv
                                virtualenv --python=python3 MyNewVirtualEnv

                      To activate this environment you simple type:
                                source MyNewVirtualEnv/bin/activate
                      All python-moduls you installed in this environment, exists only in this environment.
                      Remember : Before starting work you have to activate your virtual environment !
                      Take a look @ http://docs.python-guide.org/en/latest/dev/virtualenvs/ for further information !

    2) : We need python3:
            run:
                sudo apt-get install python3

    3) : We also need pip and the setup-tools:
            Browse to: https://pip.pypa.io/en/latest/installing.html
            download "get-pip.py"
            run:
                python get-pip.py   

    4) : We use gphoto2 to communicate with our camera :
            Browse to: http://www.gphoto.org/
            download "gphoto2"
            unzip "gphoto2" and take look at INSTALL.txt containing in the unzipped folder.
            run the installation ( e.g. ):
                ./configure
                make
                make install

    5) : We use hugin and enblend for stitching and improving our pictures :
            Browse to: http://hugin.sourceforge.net/download/
            Read the install-instruction for your system.
            E.g. for Linux, Ubuntu :
   
                sudo add-apt-repository ppa:hugin/hugin-builds
                sudo apt-get update
                sudo apt-get install hugin enblend
                
    6) : We use the schunk-modul to communicate with the varisphear :
            Take a look @ https://pypi.python.org/pypi/SchunkMotionProtocol for install-instructions

    7) : For the communication with the varisphear we also have to do some other creepy stuff idontknowbutmatthiaswillshowusfooobaaaa...

Getting started :

    I already mentioned the tutorial , didn´t I ?
    
    1) : create a config-file or copy/edit the example one.
         creating a new one can easily be done by python checkDependcies --configfile myConfig.cfg

    2) : create an output folder for your picture ( I think you know how to do that )

    3) : Edit your configfile the way you like

    4) : connect the varisphear and run  " python checkDependcies " to check everything ! 
            
