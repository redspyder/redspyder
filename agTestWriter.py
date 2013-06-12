import agTemplateParse
import os
from agSettings import *
##################################################################################################################################
# Class agTestWriter
# Author: Jeff Toy
# Description:
#   agTestWriter creates a file named tests.txt in a students subfolder with one command with appropriate flags per line.
# Input:
#   student folder and test list output from agTestParse
# output:
#   tests.txt, a text file containing a list of commands to execute tests of student submission
# preconditions:
#   existence of template.xml file in student folder
# Usage:
#   See example usage at end of file
##################################################################################################################################

class agTestWriter:

    # Constructor
    def __init__(self):
        self.commandList = []

    def createTestFile(self, folder, testlist):
        self.commandList = []
        currentfolder = os.getcwd()
        os.chdir(folder)
        self.outputFile("\n-------------Begin Stage 3----------------\n")
        if(self.checkPreviousStage(STAGE2_SUCCESS)):
            template = agTemplateParse.agTemplateParse(STUDENT_XML) 
            if(template.getErrs() == 0):    
                for test in testlist:
                    teststring = self.getTestString(template,test)
                    self.commandList.append(teststring)
                self.outputTestFile()        
            else:
                self.outputFile('Errors in template.xml File\n')
        else:
            self.outputFile('Stage 2 Not Completed\n')
        os.chdir(currentfolder)

    def outputTestFile(self):
        f = open(TEST_COMMAND_FILE, 'w')
        for cmd in self.commandList:
            f.write(cmd+"\n")
        f.close()

    def outputFile(self, out):
        f = open(STAGE3_OUTFILE, 'a')
        f.write(out)
        f.close()

    def checkPreviousStage(self, filename):
        if(os.path.isfile(filename)):
            return(True)
        return(False)
    
    def getTestString(self,tmpl, test):
        command = tmpl.getProgramName() + " "
        for arg in test:    
            if(arg[1] != None):
                command += tmpl.getFlag(arg[0]) + " " + arg[1] + " "
            else:
                command += tmpl.getFlag(arg[0]) + arg[1] + " "
        return(command)                

## example usage:
#r = agTestWriter()
#r.createTestFile("Student1",[[('LIST_CONTENTS_SHORT', 'blah'), ('LIST_CONTENTS_LONG', '')]])



