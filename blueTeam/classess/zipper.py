import pyzipper
from datetime import datetime
from getpass import getpass
import os
from time import sleep
#===== Variables ======#
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%m%d%y")

## Compressing the files to a zip file with password
def compressFile(folder_name):
    zip_file_location = f"./{dt_string}.zip"
    zipPW = getpass("Enter password ")
    if zipPW == "":
        zipPW = "mochi"
    to_zip = list()

    with pyzipper.AESZipFile(os.path.abspath(zip_file_location), 'w', compression=pyzipper.ZIP_LZMA) as zf:
        zf.setpassword(bytes(zipPW, "utf-8"))
        zf.setencryption(pyzipper.WZ_AES, nbits=128)
        for root,dirs,files in os.walk(folder_name):
            for filed in files:
                zf.write(f"{root}/{filed}")
        zf.close()
    return os.path.abspath(zip_file_location)
    
# Extracting zipfiles
def extractFile(file_name):
    with pyzipper.AESZipFile(file_name) as zf:
        user_location = "./"
        user_password = getpass("Enter your password: ")
        zf.setpassword(bytes(user_password, "utf-8"))
        zf.extractall(os.path.abspath(user_location))
        zf.close()
    print("extracting....")
    sleep(2)
    