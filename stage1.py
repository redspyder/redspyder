import agCompile
import agGetSubFolders
import decompressor

def run(folder):
    gf = agGetSubFolders.agGetSubFolders(folder)

    folders = gf.getFolders()
    for folder in folders:
        decompressor.decompress(folder)

run("not_tarfile/Archive.zip");
