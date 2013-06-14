#! /user/bin/python

import sys
import os
import tarfile

def decompress(path):
#    print 'starting decompress'
    output = open("stage1.out", "w")
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = output
    sys.stderr = output
    print "\n-------------Begin Stage 1----------------\n"

    if os.path.isdir(path):
        print 'directory detected: %s' % path
        dir_list = os.listdir(path)
        for dir in dir_list:
            dir_path = os.path.join(path, dir)
            decompress(dir_path)
	
    elif os.path.isfile(path):
        print 'file detected: %s' % path
        dir_path = os.path.dirname(path)
			
        if (tarfile.is_tarfile(path)):
            try:
                print 'opening tarfile'
                tar = tarfile.open(path, 'r:bz2')
                tar.errorlevel == 2
                print 'extracting tarfile'
                tar.extractall(dir_path)
                print 'closing tarfile'
                tar.close()
                print("Stage 1: decompressed %s" % dir_path)
                os.renames("stage1.out", "%s/stage1.out" % dir_path)
                
                currentfolder = os.getcwd()
                subfolder = os.path.dirname(path)
                print subfolder
                os.chdir(subfolder)
                s = open('stage1.success', 'w')
                print 'created success file'
                s.close()
                os.chdir(currentfolder)

            except:
                print "Error extracting tarfile..."
                os.renames("stage1.out", "%s/stage1.out" % dir_path)
        else:
            print "File is not a tarfile..."
            os.renames("stage1.out", "%s/stage1.out" % dir_path)
    print "\n-------------End Stage 1------------------\n"
    output.close()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
#    print 'completed decompressing...'

decompress('hw3/jack')
