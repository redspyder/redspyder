import agCompile
import agGetSubFolders

def run(folder):
    gf = agGetSubFolders.agGetSubFolders(folder)  #instantiate agGetSubFolder object
    c = agCompile.agCompile()         #instantiate agCompile object
    folders = gf.getFolders()     #get student folder list
    for f in folders:
        c.runMake(f)

## for testing stage 2, uncomment the next line, modify the argument appropriately and run this file:
#run("HW2")
