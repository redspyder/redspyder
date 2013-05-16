import xml.etree.ElementTree as ET
import os
##################################################################################################################################
# Class agTestParse
# Author: Jeff Toy
# Usage:
#   agTestParse(Template File).getTests()
#       Template File: xml file of tests defined by instructor
# return:
#   List of lists of test arguments, one per test: [["LIST_CONTENTS_SHORT","LIST_CONTENTS_LONG"],[],..], e.g. {"LIST_CONTENTS_SHORT":"-t"}
# output:
#   STAGE3_OUTFILE if xml file is incorrect
##################################################################################################################################

class agTestParse:

    #Constructor
    def __init__(self, folder, testfile):
        self.testfile = testfile
        self.topfolder = folder
        self.testlist = []
        self.errs = 0
        currentfolder = os.getcwd()
        os.chdir(folder)
        try:
            self.tree = ET.parse(testfile) 
            self.root = self.tree.getroot()
        except:
            self.malformedFile(0)

        if(self.errs == 0):
            self.checkFile()
        if(self.errs == 0):
            self.buildTestList()
        os.chdir(currentfolder)

    def malformedFile(self,code):
        f = open(STAGE3_OUTFILE, 'a')
        if(code == 0):
            f.write("Error code 0, improper xml\n")
        if(code == 1):
            f.write("Error code 1, improper tags\n")
        if(code == 2):
            f.write("Error code 2, missing name attribute\n")
        if(code == 3):
            f.write("Error code 3, missing flag\n")
        f.close()
        self.errs = 1
            
    def checkFile(self):
        if(self.root.tag != "TESTS"):
            self.malformedFile(1)
        else:
            for child in self.root: 
                if(child.tag != "TEST"):
                    self.malformedFile(1)
                for arg in child:
                    if(arg.tag != "ARGUMENT"):
                        self.malformedFile(1)
                    if(arg.attrib.keys() != ["name"]):
                        self.malformedFile(2)
                    else:
                        if(arg.attrib["name"] == None):
                            self.malformedFile(2)

    def buildTestList(self):
        for test in self.root:
            tmp = []
            for arg in test:
                if(arg.text):
                    tmp.append((arg.attrib["name"],arg.text))
                else:
                    tmp.append((arg.attrib["name"],""))
        
            self.testlist.append(tmp)


    def getErrs(self):
        return(self.errs)
        
    def getTestList(self):
        return(self.testlist)

# End Class ParseXML
#################################################################    

