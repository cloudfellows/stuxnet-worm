from os import remove, removedirs
from shutil import rmtree

# removing a file
def remove_file(filename):
    remove(filename)
    
# removing a folder
def remove_folder(directory):
    rmtree(directory)