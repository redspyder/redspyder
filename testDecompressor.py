import decompressor
import unittest
import os

CWD = os.getcwd()
FILEPATH = CWD + '/test_files'

class PositiveTestCase(unittest.TestCase):
	def runTest(self):
		"""Positive test case"""
		check = ['CS311_Assn5_writeup.pdf',	'ProcBenchmarker.sh', 'ThreadBenchmarker', 'makefile', 'proj5_multi_proc.c', 'proj5_threadstest.c']
		decompressor.decompress(FILEPATH)
		files = os.listdir(FILEPATH)
		for c in check:
			self.assertIn(c, files)
	
## Negative test cases
class FileNotFoundCase(unittest.TestCase):
	def runTest(self):
		"""Negative test case"""
		decompressor.decompress(CWD)
		
	
if __name__ == '__main__':
    unittest.main()