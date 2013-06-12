import sys
import os
import tarfile

import agGetSubFolders
#from decompressor import *                                                     

def run(folder):
    gf = agGetSubFolders.agGetSubFolders(folder)
    folders = gf.getFolders()
    for fold in folders:
        print fold
        print 'extracting %s' % fold
        decompress(fold)
        print 'completed extraction: %s' % fold

def decompress(path):
    print 'finished decomping'

run('hw3')
