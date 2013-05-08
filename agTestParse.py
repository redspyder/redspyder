import xml.etree.ElementTree as ET

##################################################################################################################################
# Class agTestParse
# Author: Jeff Toy
# Usage:
#   agTestParse(Template File).getTests()
#       Template File: xml file of tests defined by instructor
# return:
#   List of lists of test arguments, one per test: [["LIST_CONTENTS_SHORT","LIST_CONTENTS_LONG"],[],..], e.g. {"LIST_CONTENTS_SHORT":"-t"}
# output:
#   errors.txt if xml file is incorrect
##################################################################################################################################

class agTestParse:
    testlist = []
    #Constructor
    def __init__(self, test_file):
        assert(test_file != "")
        self.test_file = test_file
        self.errs = 0

        try:
            self.tree = ET.parse(test_file) 
            self.root = self.tree.getroot()
        except:
            self.malformedFile(0)

        if(self.errs == 0):
            self.checkFile()
        if(self.errs == 0):
            self.buildTestList()

    def malformedFile(self,code):
        f = open('errors.txt', 'a')
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
        # TODO: Revise this
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
        
    def getTests(self):
        return(self.testlist)

# End Class ParseXML
#################################################################    

