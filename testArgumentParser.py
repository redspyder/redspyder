import argumentParser
from agSettings import *
import unittest
import sys

class TestArgumentParser(unittest.TestCase):
	
	def setUp(self):
		self.var = "blah"

	def test_hwFolder(self):
		self.assertEqual(parse.getFolder(), self.getCommandLineFolder()[0])

	def test_stage(self):
		self.assertEqual(self.var, "blah")

	def test_timeout(self):
		self.assertEqual(self.var, "blah")

	def test_testFile(self):
		self.assertEqual(self.var, "blah")

	def test_template(self):
		self.assertEqual(self.var, "blah")

	def getCommandLineFolder(self):
		return(argslist)
		
if __name__ == '__main__':
	argslist = ['HW2','--stage=1', '--timeout=10', '--test=tests.xml']
	for arg in argslist:
		sys.argv.append(arg)
	print sys.argv
	parse = argumentParser.ParseArgs()
	del sys.argv[1:]
	unittest.main()		
