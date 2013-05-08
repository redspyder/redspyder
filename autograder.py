import argumentParser
import decompressor
import agCompile
import agTestExecutor
import uploader
import sys
import os

args = argumentParser.parseArgs(sys.argv)

print args

## all student folders in homework folder
students = os.listdir(args.hw_folder)

## Stage 1 = decompression
if 1 in args.stage:
	for each s in students:
		decompressor.decompress(s)
	## if error that prevents continuation occurs, exit program
	
## Stage 2 = compilation
if 2 in args.stage:
	for each s in students:
		agCompile(students)
	## if error that prevents continuation occurs, exit program

## Stage 3 = testing
if 3 in args.stage:
	for each s in students:
		for each test in args.test:
			agTestExecutor(test)

## Stage 4 = reporting
if 4 in args.stage:
	for each s in students:
		uploader.reporter(s, args.hw_folder)
		for each st in args.stage:
			s_rep = s + '/report.txt'
			uploader.uploader(s, args.hw_folder, st, s_rep)