import sys
import os
import tarfile

import agCompile
import agGetSubFolders
import decompressor

def run(folder):
    gf = agGetSubFolders.agGetSubFolders(folder)
    folders = gf.getFolders()
    print folders
    for fold in folders:
        print 'extracting %s' % fold
        decompressor.decompress(fold)
        print 'completed extraction: %s' % fold

run("hw3");
