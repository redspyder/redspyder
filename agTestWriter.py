import ParseTemplate
import ParseTests

##################################################################################################################################
# Class agTestWriter
# Author: Jeff Toy
# Usage:
# output:
##################################################################################################################################

#TODO: move code to class agTestWriter

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


