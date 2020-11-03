from os import remove, removedirs
from shutil import rmtree

def remove_file(filename):
    remove(filename)

def remove_folder(directory):
    rmtree(directory)