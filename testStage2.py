import stage2
import unittest
import os

CWD = os.getcwd()
GOOD_FOLDER = CWD + '/compiler_tests/good'
EMPTY_FOLDER = CWD + '/compiler_tests/empty'
BAD_MAKE = CWD + '/compiler_tests/bad_make'
NO_MAKE = CWD + '/compiler_tests/no_make'

class PositiveTestCase(unittest.TestCase):
	def runTest(self):
		"""Positive test case"""
		stage2.run(GOOD_FOLDER)		
		files = os.listdir(GOOD_FOLDER)
		check = ['stage2.out','prog419']
		for c in check:
			self.assertIn(c, files)
			
class EmptyFolderTestCase(unittest.TestCase):
	def runTest(self):
		stage2.run(EMPTY_FOLDER)
		files = os.listdir(EMPTY_FOLDER)
		check = 'stage2.out'
		checkNot = 'prog419'
		self.assertNotIn(checkNot, files)
		self.assertIn(check, files)

class BadMakefileFolder(unittest.TestCase):
	def runTest(self):
		stage2.run(BAD_MAKE)
		files = os.listdir(BAD_MAKE)
		check = 'stage2.out'
		checkNot = 'prog419'
		self.assertNotIn(checkNot, files)
		self.assertIn(check, files)

class MissingMakefileCase(unittest.TestCase):
	def runTest(self):
		stage2.run(NO_MAKE)
		files = os.listdir(NO_MAKE)
		check = 'stage2.out'
		checkNot = 'prog419'
		self.assertNotIn(checkNot, files)
		self.assertIn(check, files)
		

	
if __name__ == '__main__':
	unittest.main()