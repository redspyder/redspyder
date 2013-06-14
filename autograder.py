import argumentParser
import sys
import stage1
import stage2
import stage3
import stage3_5
import stage4
#import uploader

args = argumentParser.ParseArgs()

## if no argument for stage provided, assume running all
if args.getStage() == []:
	args.stage = [1, 2, 3, 4]

## Stage 1 = decompression
if 1 in args.getStage():
	print "---Begin Stage 1---"
	stage1.run(args.getFolder())
	print "---End Stage 1-----"
	## if error that prevents continuation occurs, exit program
	
## Stage 2 = compilation
if 2 in args.getStage():
	print "---Begin Stage 2---"
	stage2.run(args.getFolder())
	print "---End Stage 2-----"
	## if error that prevents continuation occurs, exit program

## Stage 3 = testing
if 3 in args.getStage():
	print "---Begin Stage 3---"
	stage3.run(args.getFolder(), args.getTimeout(), args.getTest())
	print "---End Stage 3-----"

## Stage 3.5 = uploading
if (1 in args.getStage() or 2 in args.getStage() or 3 in args.getStage()):
	print "---Begin Stage 3.5---"
	stage3_5.run(args.getFolder())
	print "---End Stage 3.5-----"

## Stage 4 = reporting
if 4 in args.getStage():
	print "---Begin Stage 4---"
	stage4.run(args.getFolder())
	print "---End Stage 4-----"

## Upload if needed
#if (1 in args.getStage() or 2 in args.getStage() or 3 in args.getStage()):
#	print "uploading to db"
#	uploader()
