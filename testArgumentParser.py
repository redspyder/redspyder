import argumentParser
from agSettings import *
import unittest
import sys

class TestArgumentParser(unittest.TestCase):

	def setUp(self):
		self.var = "setup section"
		
	def test_hwFolder(self):
		sys.argv = ["autograder.py", "H3453"]
		parse = argumentParser.ParseArgs()
		self.assertEqual(parse.getFolder(), "H3453")

	def test_stage(self):
		sys.argv = ["autograder.py", "H3453","--stage=1"]
		parse = argumentParser.ParseArgs()
		self.assertEqual(parse.getStage(), [1])
		sys.argv = ["autograder.py", "H3453","--stage=1","--stage=2"]
		parse = argumentParser.ParseArgs()
		self.assertEqual(parse.getStage(), [1,2])

	def test_timeout(self):
		sys.argv = ["autograder.py", "H3453","--timeout=1"]
		parse = argumentParser.ParseArgs()
		self.assertEqual(parse.getTimeout(), 1)

	def test_testFile(self):
		sys.argv = ["autograder.py", "H3453","--test=test.xml"]
		parse = argumentParser.ParseArgs()
		self.assertEqual(parse.getTest(), "test.xml")

if __name__ == '__main__':
	unittest.main()		



