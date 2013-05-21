import stage4
import unittest


class PositiveTestCase(unittest.TestCase):
	def runTest(self):
		"""Positive test case"""
		stage2.run("hw3")		
	

	
if __name__ == '__main__':
	unittest.main()