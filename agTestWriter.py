import agTemplateParse
import agTestParse
import os
##################################################################################################################################
# Class agTestWriter
# Author: Jeff Toy
# Usage:
#   agTestWriter(folder,template xml file,test xml file).outputTestFile()
#       folder: folder containint template xml file and test xml file
#       template xml File: xml file of students command line arguments
#       test xml file: xml file of tests defined by instructor
# output:
#   tests.txt, a text file containing a list of commands to execute tests of student submission
##################################################################################################################################

class agTestWriter:

    # Constructor
    def __init__(self, folder, template_xml, test_xml):
        assert(folder != "")
        assert(template_xml != "")
        assert(test_xml != "")
        self.commandList = []
        self.folder = folder
        self.template_xml = template_xml
        self.test_xml = test_xml
        self.errs = 0
        os.chdir(folder)
        self.createTestCommandList()

    def createTestCommandList(self):
        template = agTemplateParse.agTemplateParse("template.xml")
        tests = agTestParse.agTestParse("test.xml")
        if(template.getErrs()==0 and tests.getErrs()==0):
            for test in tests.getTests():
                self.commandList.append(self.getTestCommand(template.getTemplateDict(), test))


    def outputTestFile(self):
        f = open('tests.txt', 'w')
        for cmd in self.commandList:
            f.write(cmd+"\n")
        f.close()
    
    
    def getTestCommand(self,tmplDict, test):
        command = tmplDict["Program"] + " "
        for arg in test:    
            if(arg[1] != None):
                command += tmplDict[arg[0]] + " " + arg[1] + " "
            else:
                command += tmplDict[arg[0]] + arg[1] + " "
        return(command)                

#example usage:
#r = agTestWriter("./TestWriter","template.xml","test.xml").outputTestFile()


