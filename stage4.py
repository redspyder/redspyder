import uploader
import agGetSubFolders
import os

def run(folder):
	gf = agGetSubFolders.agGetSubFolders(folder)
	subfolders = gf.getFolders()   
	
	for f in subfolders:
		# Get all stage files
		files = os.listdir(subfolder)
		if 'stage1.out' in files:
			uploader.upload(subfolder, folder, 1, 'stage1.out') #upload stage 1 results
		if 'stage2.out' in files:
			uploader.upload(subfolder, folder, 2, 'stage2.out') #upload stage 2 results
		if 'stage3.out' in files:
			uploader.upload(subfolder, folder, 3, 'stage3.out') #upload stage 3 results
		
		uploader.reporter(subfolder, folder) # generate report