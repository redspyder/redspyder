import reporter
import agGetSubFolders
from agSettings import *

def run(folder):
	gf = agGetSubFolders.agGetSubFolders(folder)
	subfolders = gf.getFolders()   
	
	for subfolder in subfolders:
		reporter.reporter(subfolder, folder) # generate report


