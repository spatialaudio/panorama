
class BatCreator:

    ''' Create the Bat-files for stiching'''

    def __init__(self, hugin_dir):
        self.hugin_dir = str(hugin_dir)

    def create_ptsticher(self):
        ''' Creates the bat-file for stiching the pictures using our PtSticher File '''

        data = '"' + self.hugin_dir + \
            '\\bin\\nona" -o panorama pt_file.txt\r\n"'
        data += self.hugin_dir + '\\bin\enblend" -o panorama.tif *.tif\r\n'
        data += 'REM del  /s /q temp\r\nREM rmdir  /s /q temp\r\npause'

        return data

    def create_scripted(self):
        ''' Creates the bat-file for stiching the pictures using the "typical" way. '''

        data = 'MD temp\r\n\r\n\r\n"'
        data += self.hugin_dir + \
            '\\bin\pto_gen" 		-o 		"temp\project.pto" *.jpg\r\n"'
        data += self.hugin_dir + \
            '\\bin\cpfind" 		-o 		"temp\project.pto" --multirow --celeste "temp\project.pto"\r\n'
        data += 'REM "' + self.hugin_dir + \
            '\\bin\cpfind" 		-o 		"temp\project.pto" --celeste "temp\project.pto"\r\n'
        data += '"' + self.hugin_dir + \
            '\\bin\cpclean" 		-o 		"temp\project.pto" "temp\project.pto"\r\n\r\n\r\n'
        data += 'REM"' + self.hugin_dir + \
            '\\bin\pto_var" --set" TrX=-56.464036 , TrY=-73.509910, TrZ=98.405626,'
        data += 'a=0.005696 , b=-0.021579 , c=0.009606 , d=1-a-b-c" "temp\project.pto"\r\n\r\n'
        data += '"' + self.hugin_dir + \
            '\\bin\linefind" 	-o 		"temp\project.pto" "temp\project.pto"\r\n'
        data += '"' + self.hugin_dir + \
            '\\bin\\autooptimiser" 	-a -m -l -s -o 	"temp\project.pto" "temp\project.pto"\r\n'
        data += 'REM"' + self.hugin_dir + \
            '\\bin\\autooptimiser" 	-n -o 		"temp\project.pto" "temp\project.pto"\r\n'
        data += '"' + self.hugin_dir + \
            '\\bin\pano_modify" 	--canvas=AUTO --crop=AUTO -o '
        data += '"temp\project.pto" "temp\project.pto"\r\n"'
        data += self.hugin_dir + \
            '\\bin\nona" -o temp\out -m TIFF_m "temp\project.pto"\r\n'
        data += '"' + self.hugin_dir + \
            '\\bin\enblend" -o panorama.tif "temp\*.tif"\r\n'
        data += 'REM del  /s /q temp\r\nREM rmdir  /s /q temp\r\npause'

        return data

    def create_template(self):
        ''' Creates the bat-file for stiching the pictures using our template '''

        data = '"' + self.hugin_dir + \
            '\\bin\\nona" -o temp\out -m TIFF_m "temp\project.pto" '
        data += 'a_0.jpg a_1.jpg a_2.jpg a_3.jpg a_4.jpg a_5.jpg a_6.jpg a_7.jpg '
        data += 'a_8.jpg a_9.jpg a_10.jpg b_0.jpg b_1.jpg b_2.jpg b_3.jpg b_4.jpg '
        data += 'b_5.jpg b_6.jpg b_7.jpg b_8.jpg b_9.jpg b_10.jpg c_0.jpg c_1.jpg '
        data += 'c_2.jpg c_3.jpg c_4.jpg c_5.jpg c_6.jpg c_7.jpg c_8.jpg c_9.jpg '
        data += 'c_10.jpg d_0.jpg d_1.jpg d_2.jpg d_3.jpg d_4.jpg d_5.jpg d_6.jpg '
        data += 'd_7.jpg d_8.jpg d_9.jpg d_10.jpg e_0.jpg e_1.jpg e_2.jpg e_3.jpg '
        data += 'e_4.jpg e_5.jpg e_6.jpg e_7.jpg e_8.jpg e_9.jpg e_10.jpg\r\n'
        data += '"' + self.hugin_dir + \
            '\\bin\enblend" -o panorama.tif "temp\*.tif"\r\n'
        data += 'REM del  /s /q temp\r\nREM rmdir  /s /q temp\r\npause'

        return data
