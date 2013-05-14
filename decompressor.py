#! /user/bin/python

import sys
import os
import tarfile

def decompress(path):
    output = open("output.txt", "w")
    sys.stdout = output
    sys.stderr = output

    if os.path.isdir(path):
        dir_list = os.listdir(path)
        for dir in dir_list:
            dir_path = os.path.join(path, dir)
            decompress(dir_path)
	
    elif os.path.isfile(path):
        dir_path = os.path.dirname(path)
			
        if (tarfile.is_tarfile(path)):
            tarfile.open(path, 'r:bz2').extractall(dir_path)
            print("Stage 1: decompressed %s" % dir_path)
            open("output1.txt", "w")
            os.renames("output.txt", "%s/output1.txt" % dir_path)

    output.close()
