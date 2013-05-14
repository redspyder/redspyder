import os, subprocess, time

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
        
    def errorFile(self, err):
        f = open('errors.txt', 'a')
        f.write(err)
        f.close()

    def getErrors(self):
        return(self.errs)
        
    def outputFile(self, out):
        f = open('output.txt', 'a')
        f.write(out)
        f.close()
                
    def runMake(self,folder):
        currentFolder = os.getcwd()
        os.chdir(folder)
        if(os.path.isfile("./makefile") or os.path.isfile("./Makefile")):
            popen = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out,err = popen.communicate()
            self.outputFile(out)
            self.errorFile(err)
        else:
            self.errorFile("Did not find a makefile.\n")
        
        os.chdir(currentFolder)

## Example usage:
#r = agCompile()
#r.runMake("student1")

