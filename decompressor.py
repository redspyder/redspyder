#! /user/bin/python

import sys
import os
import tarfile

def decompress(path):
    output = open("stage1.out", "w")
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
            try:
                tar = tarfile.open(path, 'r:bz2')
                tar.errorlevel == 2
                tar.extractall(dir_path)
                tar.close()
                
                print("Stage 1: decompressed %s" % dir_path)
                os.renames("stage1.out", "%s/stage1.out" % dir_path)
                success = open("stage1.success", "w")
                success.close()

            except tarfile.TarError:
                print "Error extracting tarfile..."
        else:
            print "File is not a tarfile..."

    output.close()
