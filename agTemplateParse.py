import xml.etree.ElementTree as ET

##################################################################################################################################
# Class agTemplateParse
# Author: Jeff Toy
# Usage:
#   agTemplateParse(Template File).getTemplateDict()
#       Template File: xml file of students command line arguments
# return:
#   Dictionary of entries: {argument title:argument}, e.g. {"LIST_CONTENTS_SHORT":"-t"}
# output:
#   errors.txt if xml file is incorrect
##################################################################################################################################

class agTemplateParse:
    templateDict = {}
    # Constructor
    def __init__(self, template_file):
        assert(template_file != "")
        self.template_file = template_file
        self.errs = 0
        try:
            self.tree = ET.parse(template_file) 
            self.root = self.tree.getroot()
        except:
            self.malformedFile(0)
        if(self.errs == 0):
            self.checkFile()
        if(self.errs == 0):
            self.buildDict()

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

        if(self.root.tag != "PROGRAM"):
            self.malformedFile(1)
        if(self.root.attrib.keys() != ["name"]):
            self.malformedFile(2)
        else:
            if(self.root.attrib["name"] == None):
                self.malformedFile(2)
            
        for child in self.root: 
            if(child.tag != "ARGUMENT"):
                self.malformedFile(1)
            if(child.attrib.keys() != ['name']):
                self.malformedFile(2)
            if(child.text == None):
                self.malformedFile(3)
        
    def getErrs(self):
        return(self.errs)                    

    def buildDict(self):
        self.templateDict = {"Program":self.root.attrib["name"]}
        for arg in self.root:
            self.templateDict[arg.attrib["name"]] = arg.text

    def getTemplateDict(self):
        return self.templateDict        


# End Class ParseTemplate
#################################################################
