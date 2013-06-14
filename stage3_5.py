import uploader
import agGetSubFolders
import os
from agSettings import *

def run(folder):
	gf = agGetSubFolders.agGetSubFolders(folder)
	subfolders = gf.getFolders()   
	for subfolder in subfolders:
		# Get all stage files
		files = os.listdir(subfolder)
		if STAGE1_OUTFILE in files:
			if STAGE1_SUCCESS in files:
				uploader.uploader(subfolder, subfolder.rpartition('/')[2],folder, "stage1", STAGE1_OUTFILE, "Passed") #upload stage 1 results
			else:
				uploader.uploader(subfolder, subfolder.rpartition('/')[2],folder, "stage1", STAGE1_OUTFILE, "Failed") #upload stage 1 results
		if STAGE2_OUTFILE in files:
			if STAGE2_SUCCESS in files:
				uploader.uploader(subfolder, subfolder.rpartition('/')[2],folder, "stage2", STAGE2_OUTFILE, "Passed") #upload stage 2 results
			else:
				uploader.uploader(subfolder, subfolder.rpartition('/')[2],folder, "stage2", STAGE2_OUTFILE, "Failed") #upload stage 2 results
		if STAGE3_OUTFILE in files:
			if STAGE3_SUCCESS in files:
				uploader.uploader(subfolder, subfolder.rpartition('/')[2],folder, "stage3", STAGE3_OUTFILE, "Passed") #upload stage 3 results
			else:
				uploader.uploader(subfolder, subfolder.rpartition('/')[2],folder, "stage3", STAGE3_OUTFILE, "Failed") #upload stage 3 results
		

