import agGetSubFolders
import agTestParse
import agTestWriter
import agTestExecutor

# arguments:
#   folder: (string) top level folder, e.g. "HW3"
#   timeout: (integer) timeout for execution of each test in minutes
#   testfile: (string) name of instructor generated test file located in top level folder, e.g. "tests.xml"

def run(folder, timeout, testfile):                 
    gf = agGetSubFolders.agGetSubFolders(folder)    #instantiate agGetSubFolder object
    prs = agTestParse.agTestParse(folder, testfile) #instantiate agTestParse object
    wrt = agTestWriter.agTestWriter()               #instantiate agTestWriter object
    exe = agTestExecutor.agTestExecutor()           #instantiate agTestExecutor object
    
    folders = gf.getFolders()                       #get student folder list
    testlist = prs.getTestList()                    #Get python list of tests from testfile e.g. tests.xml
    for f in folders:                          #iterate over student folders
        wrt.createTestFile(f, testlist)        #create test.txt file in folder
        exe.runTests(f, timeout)               #run each line in test.txt file in folder with timeout

## for testing stage 3, uncomment the next line, modify the argument appropriately and run this file:
#run("HW2",7,"tests.xml")
