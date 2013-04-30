import xml.etree.ElementTree as ET

#################################################################
# Class ParseTests
class ParseTests:
    testlist = []
    #Constructor
    def __init__(self, test_file):
        assert(test_file != "")
        self.test_file = test_file

        try:
            self.tree = ET.parse(test_file) 
            self.root = self.tree.getroot()
        except:
            self.malformedFile()

        self.checkFile()
        self.buildTestList()

    def malformedFile(self):
        # TODO: Create error file code
        print("Error File")
            
    def checkFile(self):
        # TODO: Revise this
        if(self.root.tag != "TESTS"):
            self.malformedFile()
        else:
            for child in self.root: 
                if(child.tag != "TEST"):
                    self.malformedFile()

    def buildTestList(self):
        for test in self.root:
            tmp = []
            for arg in test:
                if(arg.text):
                    tmp.append((arg.attrib["name"],arg.text))
                else:
                    tmp.append((arg.attrib["name"],""))
        
            self.testlist.append(tmp)

    def getTests(self):
        return(self.testlist)

# End Class ParseXML
#################################################################    

