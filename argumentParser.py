import argparse
import os

class ParseArgs:
	def __init__(self):
		parser = argparse.ArgumentParser(description="Autograde assignments", prog="autograder")
		parser.add_argument('hw_folder', metavar='hw_folder', help='folder containing homework assignments')
		parser.add_argument('--stage', help='which stage of autograder to run', type=int, action='append')
		parser.add_argument('--timeout', help='timeout for autograder (in minutes)', type=int)
		parser.add_argument('--test', help='test file to run on assignment', action='append', type=argparse.FileType('r'))
		parser.add_argument('--template', help='template file submitted by students', action='append', type=argparse.FileType('r'))
		args = parser.parse_args()
		if (args.stage):
			self.stage = args.stage
		else:
			self.stage = [1, 2, 3, 4]
		self.hw_folder = args.hw_folder
		self.timeout = args.timeout
		self.test = args.test
		self.template = args.template
		
	def getFolder(self):
		return self.hw_folder
	
	def getStage(self):
		return self.stage
	
	def getTimeout(self):
		return self.timeout
		
	def getTest(self):
		return self.test
	
	def getTemplate(self):
		return self.template