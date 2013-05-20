import decompressor
import unittest
import os
import tarfile

CWD = os.getcwd()
FILEPATH = CWD + '/test_files'
EMPTY_FILEPATH = CWD + '/empty_testdir'
NOT_FOUND = CWD + '/do_not_exist'
WRONG_TYPE = CWD + '/not_tarfile'

class PositiveTestCase(unittest.TestCase):
	def runTest(self):
		"""Positive test case"""
		check = ['CS311_Assn5_writeup.pdf',	'ProcBenchmarker.sh', 'ThreadBenchmarker', 'makefile', 'proj5_multi_proc.c', 'proj5_threadstest.c']
		decompressor.decompress(FILEPATH)
		files = os.listdir(FILEPATH)
		for c in check:
			self.assertIn(c, files)
	
## Negative test cases
class NoTBZ2FileCase(unittest.TestCase):
	def runTest(self):
		"""Negative test case"""
		decompressor.decompress(EMPTY_FILEPATH)
		files = os.listdir(EMPTY_FILEPATH)
		self.assertEqual(files, [])

class FileNotFoundCase(unittest.TestCase):
	def runTest(self):
		"""File not found"""
		decompressor.decompress(NOT_FOUND)
		self.assertRaises(tarfile.TarError)

class WrongCompressionTypeCase(unittest.TestCase):
	def runTest(self):
		"""Wrong file type"""
		decompressor.decompress(WRONG_TYPE)
		self.assertRaises(tarfile.TarError)
	
if __name__ == '__main__':
	unittest.main()