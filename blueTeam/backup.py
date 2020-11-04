from classess.zipper import *
import os,shutil



def backup_da_file(zipfile):
    shutil.move(zipfile, "C:/Users/mochi/OneDrive/Backup")


## Compressing the file and getting the absolute path of the zipfile
abs_path_zipfile = compressFile("./test")
backup_da_file(abs_path_zipfile)
