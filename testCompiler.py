import agCompile
import unittest
import os

CURDIR = os.getcwd()

class PositiveTestCase(unittest.TestCase):
	def runTest(self):
		agcompile(CURDIR, "fakestring")	
class NegativeTestCase(unittest.TestCase):
	def runTest(self):
		agcompile(CURDIR, "fakestring")
		
if __name__ == '__main__':
	unittest.main()