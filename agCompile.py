import os, subprocess, time

##################################################################################################################################
# Class agCompile
# Author: Jeff Toy
# Usage:
#   agCompile(Folder, Program Name)
#       Folder: Top level folder containing student subfolders: e.g. HW3, where: HW3/student1/<assignment files>, etc.
#       Program Name: Name of the executable expected for the assignment, e.g. myar
# Output:
#   stdout if problem with parameters
#   errors.txt in student subfolder if compile errors
#   output.txt in student subfolder if no compile errors
##################################################################################################################################

class agCompile:

    def __init__(self, topHwFolder, pName):
        assert(topHwFolder != "")
        assert(pName != "")
        self.errs = 0
        self.topFolder = topHwFolder
        self.programName = pName
        if(not os.path.isdir(self.topFolder)):
            print("Invalid input folder.")
            self.errs += 1
            return
            
        self.folders = self.getSubfolders(self.topFolder)
        self.makeAll(self.folders)
        
    def errorFile(self, err):
        self.errs += 1
        f = open('errors.txt', 'a')
        f.write(err)
        f.close()

    def getErrors(self):
        return(self.errs)
        
    def outputFile(self, out):
        f = open('output.txt', 'a')
        f.write(out)
        f.close()
                
    def getSubfolders(self, parentFolder):
        folderlist = []
        os.chdir(parentFolder)
        students = os.listdir("./")
        for f in students:
            if(os.path.isdir(f)):
                folderlist.append(os.getcwd()+"/"+f)
        return(sorted(folderlist))

    def makeAll(self, folderlist):
        for f in folderlist:
            self.runMake(f)
                        
    def runMake(self,folder):
        os.chdir(folder)
        if(os.path.isfile(self.programName)):
            os.rename(self.programName, self.programName+".old("+str(time.asctime())+")")
        if(os.path.isfile("./makefile") or os.path.isfile("./Makefile")):
            popen = subprocess.Popen(["make", "--silent"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out,err = popen.communicate()
            if(os.path.isfile(self.programName)):
                self.outputFile("Output: "+out+"\n")
                self.outputFile("Warnings/Errors:\n"+err+"\n")
            else:
                self.errorFile("Failed to compile "+self.programName+" in folder "+os.getcwd()+"\n")
                self.errorFile("Warnings/Errors:\n"+err+"\n")
                
            
        else:
            self.errorFile("Did not find a makefile.\n")
        
        os.chdir("../")

# Example usage:
#r = agCompile("/home/jeff/Desktop/HW3", "randomstring")

