import argumentParser
import sys
import stage1
##import stage2
##import stage3
##import stage4
##import uploader

args = argumentParser.ParseArgs()

#print args

## if no argument for stage provided, assume running all
if args.getStage() == []:
	args.stage = [1, 2, 3, 4]

## Stage 1 = decompression
if 1 in args.getStage():
    print "---stage1---\n"
    print args.getFolder()
    stage1.run(args.getFolder())
	## if error that prevents continuation occurs, exit program
	
## Stage 2 = compilation
if 2 in args.getStage():
	print "---stage2---\n"
	print args.getFolder()
	##stage2.run(args.getFolder())
	## if error that prevents continuation occurs, exit program

## Stage 3 = testing
if 3 in args.getStage():
	print "---stage2---\n"
	print args.getFolder()
	print args.getTimeout()
	print args.getTest()
    ##stage3.run(args.getFolder(), args.getTimeout(), args.getTest())

## Stage 4 = reporting
if 4 in args.getStage():
	print "---stage4---\n"
	print args.getFolder()
	##stage4.run(args.getFolder())

## Upload if needed
if (1 in args.getStage() or 2 in args.getStage() or 3 in args.getStage()):
	print "uploading to db"
	##uploader()
