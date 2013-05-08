import shlex, subprocess

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
    def __init__(self, test_file):
        assert(test_file != "")
        self.test_file = test_file
        self.errs = 0
        self.runTests()
        
    def runTests(self):
        count = 1
        f = open(self.test_file,'r')
        for line in f:
            cmd = shlex.split(line)
            if(len(cmd) > 0):
                popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out,err = popen.communicate()
                self.outputFile("Test "+str(count)+":\n"+out+"\n")
                count += 1
        f.close()

    def outputFile(self, out):
        f = open('output.txt', 'a')
        f.write(out)
        f.close()

    def errorFile(self, err):
        self.errs += 1
        f = open('errors.txt', 'a')
        f.write(err)
        f.close()

    def getErrors(self):
        return(self.errs)

# Example usage:
#r = agTestExecutor("tests.txt")

# Example test file:
#ls -l
#ls -a
