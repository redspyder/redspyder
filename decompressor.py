#! /user/bin/python

import sys
import os
import tarfile
import bz2

def decompress(path):
	output = open("output.txt", "w")
	sys.stdout = output
	sys.stderr = output
	
	dir_list = []
	dir_path = ""
	file_path = ""
	file_name = ""
	
	if os.path.isdir(path):
		dir_list = os.listdir(path)
		for dir in dir_list:
			dir_path = os.path.join(path, dir)
			decompress(dir_path)
	
	elif os.path.isfile(path):
		file_name = os.path.basename(path)
		dir_path = os.path.dirname(path)
		
		if (path.endswith('.tar.bz2')):
			data = bz2.BZ2File(file_name)
			bz2.decompress(data)
			
		if (tarfile.is_tarfile(file_name)):
			tarfile.open(path).extractall(dir_path)

	output.close()
