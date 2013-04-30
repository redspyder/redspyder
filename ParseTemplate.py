import xml.etree.ElementTree as ET

#################################################################
# Class ParseTemplate
# Jeff Toy
class ParseTemplate:
    templateDict = {}
    # Constructor
    def __init__(self, template_file):
        assert(template_file != "")
        self.template_file = template_file

        try:
            self.tree = ET.parse(template_file) 
            self.root = self.tree.getroot()
        except:
            self.malformedFile()
        
       #self.checkFile()
        self.buildDict()

    def malformedFile(self):
        # TODO: Create error file code
        print "Error File"

    def checkFile(self):
        # TODO: Revise this

        if(self.root.tag != "PROGRAM"):
            self.malformedFile()
        else:
            for child in self.root: 
                if(child.tag != "ARGUMENT"):
                    self.malformedFile()
                if(child.attrib.keys() != ['name', 'value']):
                    self.malformedFile()

    def buildDict(self):
        self.templateDict = {"Program":self.root.attrib["name"]}
        for arg in self.root:
            self.templateDict[arg.attrib["name"]] = arg.text

    def getTemplateDict(self):
        return self.templateDict        


# End Class ParseTemplate
#################################################################
