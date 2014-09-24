# -*- coding: utf-8 -*-
from sys import stderr
import os
import subprocess


class PicImprover:

    ''' Improve our picture by using fulla'''

    def __init__(self, dir_output, fulla):

        # Check output-directory

        try:
            self.dir_outputABS = os.path.abspath(dir_output)
            print(self.dir_outputABS)
            self.list_picture = os.listdir(self.dir_outputABS)
        except:
            stderr.write(
                '''\n ERROR @PicImprover: Can´t find directory %s !
                 exit \n''' % dir_output)
            exit()

        # Check fulla

        self.fulla = fulla

        if(not os.path.isfile(self.fulla)):
            stderr.write(
                '\n ERROR @PicImprover: Can´t find fulla @%s !' % self.fulla
            )
            stderr.write(
                '''\n Type " find /* | grep fulla "
                to figure your path out !\n exit \n''')
            exit()

    def show_statistic(self, a, b, c):

        print("\n °----------------------------------------°")
        print("\n Statistic [ Improvement ]:")
        print("\n Lens correction parameters:")
        print("\n\t a: %f" % a)
        print("\n\t b: %f" % b)
        print("\n\t c: %f" % c)
        print("\n Picture will be loaded from: %s" % (self.dir_outputABS))
        print("\n Number of Pictures to improve: %d" %
              (len(self.list_picture)))
        print("\n Location of fulla: %s" % (self.fulla))
        print("\n °----------------------------------------°")

    def improve_pic(self, a, b, c):
        d = str(1.0 - (a + b + c))
        a = str(a)
        b = str(b)
        c = str(c)

        for index, picture in enumerate(self.list_picture):

            filenameABS = self.dir_outputABS + "/" + picture
            # Improvment using fulla
            print(" Improve picture %d of %d " %
                  (index + 1, len(self.list_picture)))
            print(" Title: %s" % (picture))
            if(picture.endswith('_corr.JPG')):
                print(" Picture is already corrected \n")
            else:
                cparam = '-g ' + a + ':' + b + ':' + c + ':' + d
                subprocess.call([self.fulla, cparam, filenameABS])
