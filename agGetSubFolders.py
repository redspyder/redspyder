import os

##################################################################################################################################
# Class agGetSubFolders
# Author: Jeff Toy
# Description:
#   Class for creating a list of subfolders in a folder.
# Input:
#   Top level folder
# Output:
#   List of subfolders in top level folder.  Folders are absolute paths.
# Usage:
#   See sample usage at bottom of file.  Uncomment and run this file to demonstrate.
##################################################################################################################################

class agGetSubFolders:

    def __init__(self,folder):
        assert(folder != "")
        self.folderList = []
        currentFolder = os.getcwd()
        print folder
        if(not os.path.isdir(folder)):
            print("Invalid input folder.")
            return
        os.chdir(folder)
        folderContents = os.listdir("./")
        for f in folderContents:
            if(os.path.isdir(f)):
                self.folderList.append(os.getcwd()+"/"+f)
        os.chdir(currentFolder)

    def getFolders(self):
        return(sorted(self.folderList))
        
## example usage:
#r = agGetSubFolders("HW3")
#folders = r.getFolders()
#print(folders)        
