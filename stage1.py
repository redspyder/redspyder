import agGetSubFolders
import decompressor

def run(folder):
    gf = agGetSubFolders.agGetSubFolders(folder)
    folders = gf.getFolders()
    for fold in folders:
        decompressor.decompress(fold)


