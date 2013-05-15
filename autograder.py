import argumentParser
import sys
import stage1
import stage2
import stage3
import stage4


args = argumentParser.parseArgs(sys.argv)

#print args

## if no argument for stage provided, assume running all
if args.stage == []:
	args.stage = [1, 2, 3, 4]

## Stage 1 = decompression
if 1 in args.stage:
    stage1.run(args.hw_folder)
## if error that prevents continuation occurs, exit program
	
## Stage 2 = compilation
if 2 in args.stage:
	stage2.run(args.hw_folder)
	## if error that prevents continuation occurs, exit program

## Stage 3 = testing
if 3 in args.stage:
    stage3.run(args.hw_folder, args.timeout, args.test)

## Stage 4 = reporting
if 4 in args.stage:
	stage4.run(args.hw_folder)
