import sys,os,base64
sys.version
'''
daVinciGcodePrep.py

Mason Sheffield 12/29/2014

This will take a slic3r gcode file and convert it to work with the XYZ DaVinci 3d printer.

example:
	daVinciGcodePrep.py E:/projects/newborn/newborn_printB.gcode
Process:
	1. remove all header text above and including the topLine (specified below)
	2. encode the file to base64 format
	3. Write with a 3w extension

'''
def main(myFile, curaMode=False):
	print myFile
	#myFile = 'E:/projects/newborn/newborn_printB.gcode'
	#delete this text line and all text above it
	topLine = "; --- MOVE THIS SECTION TO THE TOP AND DELETE THIS LINE ---\n"
	#read original file
	f = open(myFile)
	myLines = f.readlines()
	f.close()
	#start writing to new list after finding line matching 'topLine' 
	trimmedGcode = list()
	curaHeader = [];
	startLine = False
	for x in myLines:
		#Must replace all G0 instructions with G1 for DaVinci Printer
		if curaMode and x[:3] == 'G0 ':
			x = 'G1 ' + x[3:]
		if startLine and x != '\n':
			trimmedGcode.append(x)
		if x == topLine:
			startLine = True
		#Save the CURA header	
		if curaMode:
			if not startLine and x != '\n':
				curaHeader.append(x)
			#Move cura header under the DaVinci header
			if ';TEMPERATURES\n' == x:
				trimmedGcode += curaHeader
			
	#creat new filename with .3w extension  
	newFile =  myFile[:-5] + '3w'
	newDebugFile = myFile[:-6] + '_debug.gcode'
	df = open(newDebugFile,'w+')
	df.writelines(trimmedGcode)
	df.close()
	
	outf = open(newFile,'w+')
	#encode the modified gcode file with base64 encoding
	newGcodeStr = ''.join(trimmedGcode)
	base64_gCode = base64.standard_b64encode(newGcodeStr)
	outf.writelines(base64_gCode)
	outf.close()
	print 'Encoded Stuff \n\n\n\n'	
	print 'Success!'


if __name__ == "__main__":
	main(sys.argv[1],sys.argv[2])
	
