MD temp


"e:\Hugin\bin\pto_gen" 		-o 		"temp\project.pto" *.jpg
"e:\Hugin\bin\cpfind" 		-o 		"temp\project.pto" --multirow --celeste "temp\project.pto"
"e:\Hugin\bin\cpclean" 		-o 		"temp\project.pto" "temp\project.pto"
"e:\Hugin\bin\linefind" 	-o 		"temp\project.pto" "temp\project.pto"
"e:\Hugin\bin\autooptimiser" 	-a -m -l -s -o 	"temp\project.pto" "temp\project.pto"
"e:\Hugin\bin\pano_modify" 	--canvas=AUTO --crop=AUTO -o "temp\project.pto" "temp\project.pto"





REM __________________________________________________________________________
REM Not sure if really needed:
REM "e:\Hugin\bin\pto2mk" -o "temp\project.mk" -p prefix "temp\project.pto"
REM "e:\Hugin\bin\make" -f project.mk all clean     !!! Drops error even with
REM __________________________________________________________________________




"e:\Hugin\bin\nona" -o temp\out -m TIFF_m "temp\project.pto"
"e:\Hugin\bin\enblend" -o panorama.tif "temp\out0000.tif" "temp\out0001.tif"

del  /s /q temp
rmdir  /s /q temp
pause







REM __________________________________________________________________________
REM del out0000.tif
REM del out0001.tif
REM del project.pto
REM del project.pto
REM __________________________________________________________________________



