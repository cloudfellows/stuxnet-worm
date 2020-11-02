from os import remove, removedirs
from shutil import rmtree

def remove_file(filename, directory):
    remove(filename)
    rmtree(directory)