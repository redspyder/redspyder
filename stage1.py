import agCompile
import agGetSubFolders
import decompressor

def run(folder):
    gf = agGetSubFolders.agGetSubFolders(folder)
    folders = gf.getFolders()
    for fold in folders:
        print 'extracting %s' % fold
        decompressor.decompress(fold)

#run("not_tarfile/Archive.zip");
