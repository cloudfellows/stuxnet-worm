import os,shutil, pyzipper
from datetime import datetime
## gatting time object
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%m%d%y")

## function to compress file
def compressFile(folder_name):
    zip_file_location = f"./{dt_string}.zip"
    zipPW = "latenight"
    to_zip = list()

    with pyzipper.AESZipFile(os.path.abspath(zip_file_location), 'w', compression=pyzipper.ZIP_LZMA) as zf:
        zf.setpassword(bytes(zipPW, "utf-8"))
        zf.setencryption(pyzipper.WZ_AES, nbits=128)
        for root,dirs,files in os.walk(folder_name):
            for filed in files:
                zf.write(f"{root}/{filed}")
        zf.close()
    return os.path.abspath(zip_file_location)
## backing the file up by movign the file to the onedrive
def backup_da_file(zipfile):
    shutil.move(zipfile, "C:/Users/mochi/OneDrive/Backup")


## Compressing the file and getting the absolute path of the zipfile
abs_path_zipfile = compressFile("C:/Users/mochi/Desktop/Documents")
backup_da_file(abs_path_zipfile)
