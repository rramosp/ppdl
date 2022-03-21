import sys
from os import path

def find_local_folder():
    """
    finds the first folder named "local" searching up the folder hierarchy 
    from the current dir
    """
    curdir = path.abspath(path.curdir)
    for i in range(len(curdir.split("/"))):
        pdir = curdir + "/.."*i + "/local"
        if path.exists(pdir):
            return pdir

    ## TODO: download repo from github and move content/local to current dir
    ##       and do not raise exception
    raise ValueError("no folder 'local' found")
    
    
local_folder = find_local_folder()
import sys
sys.path.insert(0, local_folder + "/lib")

def local_(name):
    """
    return a file name relative to the local folder
    """
    return f"{local_folder}/{name}"
