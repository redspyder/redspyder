import shlex, subprocess, os
import agTimeout
from agSettings import *
##################################################################################################################################
# Class agTestExecutor
# Author: Jeff Toy
# Usage:
#   agTestExecutor(Test File)
#       Test File: text file of commands for testing student submissions.  One command per line.
# output:
#   output.txt of test results
##################################################################################################################################

class agTestExecutor:

    # Constructor
    def __init__(self):
        self.errs = 0
        
    def runTests(self, folder, timeout):
        currentfolder = os.getcwd()
        os.chdir(folder)
        count = 1
        if(os.path.isfile(TEST_COMMAND_FILE)):
            f = open(TEST_COMMAND_FILE,'r')
            for line in f:
                cmd = shlex.split(line)
                if(len(cmd) > 0):
                    prog = cmd[0]
                    cmd[0] = "./"+prog
                    out = agTimeout.agTimeout(cmd, timeout).Run()
                    self.outputFile("Test "+str(count)+":\n"+out[0]+"\n"+out[1]+"\n")
                    count += 1
            f.close()
            self.writeSuccessFile()
            self.outputFile("-------------End Stage 3------------------\n")
        else:
            self.outputFile('Failed to create tests.txt\n')
        os.chdir(currentfolder)

    def writeSuccessFile(self):
        s = open(STAGE3_SUCCESS, 'w')
        s.close()

    def outputFile(self, out):
        f = open(STAGE3_OUTFILE, 'a')
        f.write(out)
        f.close()

    def getErrors(self):
        return(self.errs)

# Example usage:
#r = agTestExecutor("tests.txt")

