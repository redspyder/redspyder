import argparse
import sys

def parseArgs(args):  
	"""Parses the command line arguments
		Keyword arguments:
		args -- array of arguments
	"""
	parser = argparse.ArgumentParser(description="Autograde assignments", prog="autograder")
	parser.add_argument('hw_folder', metavar='hw_folder',
                   help='folder containing homework assignments')
	parser.add_argument("--stage", help="which stage of autograder to run", type=int, action="append")
	parser.add_argument("--timeout", help="timeout for autograder (in minutes)", type=int)
	parser.add_argument("--test", help="test file to run on assignment", action="append", type=argparse.FileType('r'))
    parset.add_argument("--template", help="template file submitted by students", action="append", type=argparse.FileType('r'))
	args = parser.parse_args()
	
	return args
	
if __name__ == '__main__':
	args = parseArgs(sys.argv)
	print args
