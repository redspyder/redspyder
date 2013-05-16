import os, subprocess, time
import agSettings
##################################################################################################################################
# Class agCompile
# Author: Jeff Toy
# Description:
#   Class for running make in a folder
# Input:
#   folder containing makefile and code
# Output:
#   errors.txt in student subfolder if no makefile
#   output.txt in student subfolder if makefile, output of make command.
# Usage:
#   See example usage at bottom of file
##################################################################################################################################

class agCompile:

    def __init__(self):
        self.folder = ""
        
    def outputFile(self, out):
        f = open(STAGE2_OUTFILE, 'a')
        f.write(out)
        f.close()
                
    def runMake(self,folder):
        currentFolder = os.getcwd()
        os.chdir(folder)
        if(os.path.isfile(MAKEFILE_NAMES[0]) or os.path.isfile(MAKEFILE_NAMES[1])):
            popen = subprocess.Popen([COMPILE_COMMAND])
            popen.communicate()
        else:
            self.outputFile(ERROR1)
        
        os.chdir(currentFolder)

## Example usage:
#r = agCompile()
#r.runMake("student1")

