import argumentParser
import decompressor
from agCompile import *
from agTestWriter import *
from agTestExecutor import *
import uploader
import sys
import os

args = argumentParser.parseArgs(sys.argv)

print args

## if no argument for stage provided, assume running all
if args.stage == []:
	args.stage = [1, 2, 3, 4]
	
## all student folders in homework folder
students = os.listdir(args.hw_folder)

## Stage 1 = decompression
if 1 in args.stage:
    for s in students:
        s_path = os.path.join(args.hw_folder, s)
        decompressor.decompress(s_path)
## if error that prevents continuation occurs, exit program
	
## Stage 2 = compilation
if 2 in args.stage:
	for s in students:
		agCompile(args.hw_folder)
	## if error that prevents continuation occurs, exit program

## Stage 3 = testing
if 3 in args.stage:
    for s in students:
        t_path = args.hw_folder + '/' + s
        agTestWriter(t_path, args.template, args.test)
#            agTestExecutor(test)

## Stage 4 = reporting
if 4 in args.stage:
	for s in students:
		uploader.reporter(s, args.hw_folder)
		for st in args.stage:
			s_rep = s + '/report.txt'
			uploader.uploader(s, args.hw_folder, st, s_rep)
