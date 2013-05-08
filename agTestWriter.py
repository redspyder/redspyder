import ParseTemplate, subprocess
import ParseTests

##################################################################################################################################
# Class agTestExecutor
# Author: Jeff Toy
# Usage:
#   agTestExecutor(Test File)
#       Test File: text file of commands for testing student submissions.  One command per line.
# output:
#   output.txt of test results
##################################################################################################################################

def class agTestExecutor:

    # Constructor
    def __init__(self, test_file):
        assert(test_file != "")

def main():
    f = open('output.txt', 'w')
    template = ParseTemplate.ParseTemplate("template.xml")
    tests = ParseTests.ParseTests("test.xml")
    if(template.getErrs()==0 and tests.getErrs()==0):
        for test in tests.getTests():
            createTestCommands(template.getTemplateDict(), test,f)
    f.close()
    
def createTestCommands(tmplDict, test, f):
    command = tmplDict["Program"] + " "
    for arg in test:    
        if(arg[1] != None):
            command += tmplDict[arg[0]] + " " + arg[1] + " "
        else:
            command += tmplDict[arg[0]] + arg[1] + " "
    f.write(command+"\n")                


main()


