import os, subprocess, time
from agSettings import *
import agTemplateParse
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
        self.outputFile("\n-------------Begin Stage 2----------------\n")
        if(self.checkPreviousStage(STAGE1_SUCCESS)):
            popen = subprocess.Popen([COMPILE_COMMAND],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out,err = popen.communicate()
            self.outputFile(out)
            self.outputFile(err)
            self.writeSuccessFile()
        else:
            self.outputFile("Stage 1 Not Completed\n")
        self.outputFile("-------------End Stage 2------------------\n")
        os.chdir(currentFolder)

    def writeSuccessFile(self):
        if(os.path.isfile('./template.xml')):
            tmplt = agTemplateParse.agTemplateParse('./template.xml')
            prog = tmplt.getProgramName()
            if(os.path.isfile('./'+prog)):
                os.chmod(prog, 0744)
                s = open(STAGE2_SUCCESS, 'w')
                s.close()
            else:
                self.outputFile("Executable Program Not Found\n")
        else:
            self.outputFile("No template.xml File\n")
                
    def checkPreviousStage(self, filename):
        if(os.path.isfile(filename)):
            return(True)
        return(False)
        

## Example usage:
#r = agCompile()
#r.runMake("HW2/Student1")

