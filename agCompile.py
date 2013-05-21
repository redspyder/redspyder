import os, subprocess, time
from agSettings import *
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
        popen = subprocess.Popen([COMPILE_COMMAND],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out,err = popen.communicate()
        self.outputFile(out)
        self.outputFile(err)
        os.chdir(currentFolder)
        

## Example usage:
#r = agCompile()
#r.runMake("HW2/Student1")

