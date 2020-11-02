from cryptography.fernet import Fernet
import time, os

def encrptFolder(dirNames, key):
    completeFileList = list()
    fer=Fernet(key)
    for (dirPath, dirName, fileName) in os.walk(dirNames):
        completeFileList += [os.path.join(dirPath, file) for file in fileName]
    for fil in completeFileList:
        print(fil)
        encryptFile(fil, key)

def decryptFolder(dirNames, key):
    completeFileList = list()
    for (dirPath, dirName, fileName) in os.walk(dirNames):
        completeFileList += [os.path.join(dirPath, file) for file in fileName]
    for fil in completeFileList:
        print(fil)
        decryptFile(fil, key)

def encryptFile(file, key):
    
    f = Fernet(key)
    with open(file, "rb") as fileread:
        readfile = fileread.read()
    encryptFile = f.encrypt(readfile)
    with open(file, "wb") as filewrite:
        filewrite.write(encryptFile)
        time.sleep(2)
        print("file has been encrypted")

def decryptFile(file, key):
    f = Fernet(key)
    with open(file, "rb") as fileread:

        # read the encrypted data
        encrypted_data = fileread.read()

    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)

    # write the original file
    with open(file, "wb") as filewrite:
        filewrite.write(decrypted_data)
        time.sleep(2)
        print("file has been decrypted")