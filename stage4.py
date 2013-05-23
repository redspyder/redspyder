#import reporter
import agGetSubFolders
import os
from agSettings import *

def run(folder):
	gf = agGetSubFolders.agGetSubFolders(folder)
	subfolders = gf.getFolders()   
	
	for subfolder in subfolders:
		reporter.reporter(os.path.basename(subfolder), folder) # generate report

run("HW2")