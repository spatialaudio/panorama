
class PtCreator:

    ''' Create the PTSticher-input-file'''

    def __init__(self, output_dir, a, b, c):
        self.output_dir = output_dir

        # Disortion a, b, c
        self.a = a
        self.b = b
        self.c = c

    def init_file(self):
        # return first block of PTSticher-file

        string = '# PTStitcher script, written by hugin' + '\r\n'
        string += '\r\n' + 'p f2 w3000 h1500 v340  n"TIFF_m c:LZW r:CROP"'
        string += '\r\n' + 'm g1 i0 f0 m2 p0.00784314' + '\r\n'
        string += '\r\n' + '# output image lines'
        string += '\r\n'

        return string

    def create_oline(self, vertical_pos, horizontal_pos, angle, filename):
        ''' Create o-Lines.
            A o-Line contains the absolute position of one 
            picture in our panorama [ in degree ! ].
            We need one o-Line for each picture. '''

        line = 'o w1045 h697 f0 TrX0 TrY0 TrZ0'
        line += ' a' + str(self.a) + ' b' + str(self.b) + ' c' + str(self.c)
        line += ' d0 e0 g0'
        line += ' p' + str(vertical_pos) + ' r0 t0 v' + \
            str(angle) + ' y' + str(horizontal_pos)
        line += '  n"' + str(filename) + '"\r\n'

        return line

    def create_file(self, li_vertical, li_horizontal, angle):
        ''' Return the complete pt_file '''

        pt_file = self.init_file()

        li_prefix = list(map(chr, range(97, 123)))

        for index_v, pos_v in enumerate(li_vertical):

            prefix = li_prefix[index_v]

            for index_h, pos_h in enumerate(li_horizontal):

                pic = prefix + "_" + str(index_h) + ".jpg"
                pt_file += self.create_oline(-pos_v,
                                             round((360.0 - pos_h) % 360.0, 2), angle, pic)

        pt_file += '\r\n'
        return pt_file
