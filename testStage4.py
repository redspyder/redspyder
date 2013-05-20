import stage4
import unittest


class PositiveTestCase(unittest.TestCase):
	def runTest(self):
		"""Positive test case"""
		stage4.run("hw3")		
	
## Negative test cases
class StudentNotFoundCase(unittest.TestCase):
	def runTest(self):
		"""Student not found"""
		stage4.run("HW2")
		
class HomeworkNotFoundCase(unittest.TestCase):
	def runTest(self):
		"""Homework not found"""
		stage4.run("hw4")
		
class ReportGenerateFailedCase(unittest.TestCase):
	def runTest(self):
		"""Report generation failed"""
		
class WriteToDBFailedCase(unittest.TestCase):
	def runTest(self):
		"""Write to DB failed"""
	
if __name__ == '__main__':
	unittest.main()