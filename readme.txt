convert2daVinci

Mason Sheffield 2014


These config files and python scripts allow you to convert gcode from Cura and Slic3r software into 3W files that can be printed on the xyz daVinci 1.0 3d Printer.

This has been tested on Windows 7 64bit with a daVinci 1.0 printer and XYZWare version 1.1.33.3

How to install:

	1. Create a folder here:  "C:\convert2daVinci\"
	2. copy all of the files to this new folder
	3. You must have Python 2.6 or newer installed and added to your system path



How to use with Slic3r (tested on version 1.1.7):

	1. In Slic3r go to File > Load Config and choose this file  "C:\convert2daVinci\DaVinci-Slic3r-config.ini"
	2. Add your model in the plater tab and configure your print settings
	3. In the Plater tab hit the "Export G-code..." button in the lower right and choose a location
	4. A .3w file should be created next to the original gcode file that slic3r created.
	5. Drop the 3W file into the xyzware software and you should be able to print now!

	Hey it didn't work!?!
	
		If the 3w file was not created you can double check that the post processing is correctly pointing to the python script.
		The setting is found here in slic3r:   Print Settings > Output Options > Post-Processing Scripts
		This should point to the script which is here on my machine: "C:/convert2daVinci/daVinciGcodePrep.py"

	It still doesn't work :(...
		
		No worries, just drag and drop the gcode file onto this file C:\convert2daVinci\Slicer_to_DaVinci.bat and a 3W file will be created 			beside the file you just dropped onto it!


How to use with Cura(tested on version 14.12.1):

	1. In Curago to File > Open Profile.. and choose this file  "C:\convert2daVinci\DaVinci-Cura-config.ini"
	2. Add your model and configure your print settings
	3. Choose File > Save Gcode...
	4. Now drag and drop the new gcode file onto this batch file "C:\convert2daVinci\Cura_to_DaVinci.bat"
	5. Drop the new 3W file into the xyzware software and you should be able to print now!

