import agCompile
import agSettings
import unittest
import os

CWD = os.getcwd()
GOOD_FOLDER = CWD + '/compiler_tests/good'
EMPTY_FOLDER = CWD + '/compiler_tests/empty'
BAD_MAKE = CWD + '/compiler_tests/bad_make'
NO_MAKE = CWD + '/compiler_tests/no_make'

class PositiveTestCase(unittest.TestCase):
	def runTest(self):
		compile = agCompile.agCompile()
		compile.runMake(GOOD_FOLDER)
		files = os.listdir(GOOD_FOLDER)
		check = ['output2.txt','proj419']
		for c in check:
			self.assertIn(c, files)
		
class EmptyFolderTestCase(unittest.TestCase):
	def runTest(self):
		compile = agCompile.agCompile()
		compile.runMake(EMPTY_FOLDER)
		files = os.listdir(EMPTY_FOLDER)
		check = 'errors2.txt'
		checkNot = ['output2.txt', 'proj419']
		for c in checkNot:
			self.assertNotIn(c, files)
		self.assertIn(check, files)

class BadMakefileFolder(unittest.TestCase):
	def runTest(self):
		compile = agCompile.agCompile()
		compile.runMake(BAD_MAKE)
		files = os.listdir(EMPTY_FOLDER)
		check = 'errors2.txt'
		checkNot = ['output2.txt', 'proj419']
		for c in checkNot:
			self.assertNotIn(c, files)
		self.assertIn(check, files)

class MissingMakefileCase(unittest.TestCase):
	def runTest(self):
		compile = agCompile.agCompile()
		compile.runMake(NO_MAKE)
		files = os.listdir(EMPTY_FOLDER)
		check = 'errors2.txt'
		checkNot = ['output2.txt', 'proj419']
		for c in checkNot:
			self.assertNotIn(c, files)
		self.assertIn(check, files)
		
if __name__ == '__main__':
	unittest.main()