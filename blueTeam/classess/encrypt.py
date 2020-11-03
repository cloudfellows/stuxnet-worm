from cryptography.fernet import Fernet
import time, os
from .zipper import *

def encrptFolder(dirNames, key):
    completeFileList = list()
    for (dirPath, dirName, fileName) in os.walk(dirNames):
        completeFileList += [os.path.join(dirPath, file) for file in fileName]
    for fil in completeFileList:
        print(fil)
        encryptFile(fil, key)
    key_file = open(f"{dirNames}/key.key", "w")
    key_file.write(str(key, "UTF-8"))
    key_file.close()
    compressFile(dirNames)  

def encryptFile(file, key):
    
    f = Fernet(key)
    with open(file, "rb") as fileread:
        readfile = fileread.read()
    encryptFile = f.encrypt(readfile)
    with open(file, "wb") as filewrite:
        filewrite.write(encryptFile)
        time.sleep(2)
        print("file has been encrypted")
