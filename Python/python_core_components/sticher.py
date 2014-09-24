# -*- coding: utf-8 -*-
from sys import stderr
import os
import subprocess


class PicSticher:

    ''' Offers functions for stiching
         our pictures to a panorama '''

    def __init__(self, dir_output, enblend):

        # Check output-directory

        try:
            self.dir_outputABS = os.path.abspath(dir_output)
            print(self.dir_outputABS)
            self.list_picture = os.listdir(self.dir_outputABS)
        except:
            stderr.write(
                '''\n ERROR @improvementPic: Can´t find directory %s !\n
                 exit \n''' % dir_output)
            exit()

        # Check enblend

        self.enblend = enblend

        if(not os.path.isfile(self.enblend)):
            stderr.write(
                '''\n ERROR @PicSticher:
                 Can´t find enblend @%s !''' % self.enblend)
            stderr.write(
                '''\n Type " find /* | grep enblend "
                 to figure your path out !\n exit \n''')
            exit()

    def split_pics(self, orginal, stages):

        # Select pictures for stiching from self.list_picture

        list_select = []

        for picture in self.list_picture:
            if(orginal):
                if(not picture.endswith('_corr.JPG')):
                    list_select.append(picture)
            else:
                if(picture.endswith('_corr.JPG')):
                    list_select.append(picture)

        numberPictures = len(list_select)

        if((stages < 1) or (numberPictures % stages != 0)):
            stderr.write(
                '\n ERROR @splitPic: Invalid value for STAGES: %d .' % stages)
            stderr.write(
                '''\n " Pic_per_horizontalRotation * vertical_Stages
                 == Number of Pictures " is not fullfilled.''')
            stderr.write(
                '\n   Number of Pictures = %d , Stages = %d '
                % (numberPictures, stages))
            stderr.write('\n Exit \n ')
            exit()

        # the next steps depends on our order of taken pictures ( --> see
        # showInfo )
        list_select.sort()

        # mapped all picture on one horizontal rotation
        # Of course each horizontal step consist of a list of vertical pictures
        dict_picture = {}

        for index, picture in enumerate(list_select):

            horizontal_step = index % numberPictures

            if(horizontal_step in dict_picture):
                list_v = dict_picture[horizontal_step]
            else:
                list_v = []

            list_v.append(picture)
            dict_picture[horizontal_step] = list_v

        print(dict_picture)

        return dict_picture

    def show_statistic(self, dict_picture):

        print("\n °----------------------------------------°")
        print("\n Statistic [ Stiching ]:")
        print("\n Picture will be loaded from:\n   %s" %
              (self.dir_outputABS))
        print("\n Number of Pictures for stiching :\t %d" %
              (len(dict_picture)))
        print("\n Location of enblend:\t %s" % (self.enblend))
        print("\n °----------------------------------------°")

    def show_info(self):
        print("\n °----------------------------------------°")
        print(" Info to the order/process of taking picture :")
        print(
            ''' There are x vertical stages
            ( depending on the vertical aperature angle ).''')
        print(" We start with the top stage")
        print(
            ''' Each vertical stage consist of one
            horizontal Rotation ( == 360° ).''')
        print(
            ''' Each horizontal Rotation consist of y steps
             ( depending on horizontal aperature angle ).''')
        print(" In each step we take one picture.")
        print(
            ''' The order of your pictures ( sorted by date )
             must be the follow :''')
        print("\n    < start with first taken picture > ")
        print("    top vertical stage  , first   horizontal step ")
        print("    top vertical stage  , secound horizontal step ")
        print("    top vertical stage  , ..... ")
        print("    top vertical stage  , last    horizontal step ")
        print("    < now the same just one vertical stage lower >")
        print("    lower vertical stage, first    horizontal step ")
        print("    < till the last ( bottom ) vertical stage >")
        print("    bottom vertical stage, first    horizontal step ")
        print("    bottom vertical stage  , ..... ")
        print("    bottom vertical stage  , last    horizontal step ")
        print(
            '''\n Additional to this the equation: \n
            " Pic_per_horizontalRotation * vertical_Stages ==
             Number of Pictures "\n have to be fullfilled''')
        print(
            ''' For this purpose the Number of vertical_Stages
            will be load from the config-file
             ( unless you specify it via --stages ).''')
        print(
            '''\n If the pictures in your folder fullfill this
             requirements you can use "stichPicture" for stichung
             your 360° sphaere panorama. ''')
        print(
            '''\n Picture that are created with the varispear and
             takePicture meets this requirements automatically.''')
        print("\n °----------------------------------------°")

    def stich_pictures(self, dict_picture):

        for horizontal_step in dict_picture:

            vertical_panorama = None

            list_v = dict_picture[horizontal_step]
            print(str(list_v))
            for picture in list_v:

                if vertical_panorama is None:
                    vertical_panorama = picture
                    cparam = '-g ' + a + ':' + b + \
                        ':' + c + ':' + d + ' -o _tesst'

                    '#subprocess.call([self.enblend,cparam,filenameABS])'

                else:
                    # stich vertical_panorama + picture
                    pass
