import stage3
import agGetSubFolders
import agTestParse
import agTestWriter
import agTestExecutor

import os
import unittest

class preTest():
    def __init__(self):
        self.prs = []
        self.students = []
        self.subFolderTest()
        self.testParseTest()
        self.testTestWriter()
        self.testTestExecutor()

    def subFolderTest(self):
        fg = agGetSubFolders.agGetSubFolders("hw3")
        self.students = fg.getFolders()
        for f in self.students:
            print f
            
    def testParseTest(self):
        obj = agTestParse.agTestParse("hw3", "test.xml")
        self.prs = obj.getTestList()
        print self.prs
        
    def testTestWriter(self):
        for student in self.students:
            wrt = agTestWriter.agTestWriter()
            wrt.createTestFile(student, self.prs)
            if 'tests.txt' in os.listdir(student):
                print 'tests.txt created'

    def testTestExecutor(self):
        for student in self.students:
            exe = agTestExecutor.agTestExecutor()
            exe.runTests(student, 7)
            if 'stage3.success' in os.listdir(student):
                print 'stage3.success created'


class PositiveTestCase(unittest.TestCase):
    def runTest(self):
        stage3.run("hw3", 7, "test.xml")
        files = os.listdir(".")
        self.assertIn("stage3.success", files)

if __name__ == '__main__':
    preTest()
    unittest.main()
