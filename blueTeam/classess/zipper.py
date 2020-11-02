from zipfile import *
from datetime import datetime
from getpass import getpass
import os
#===== Variables ======#
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d%m%y-%H%M")
zip_file_location = f"./{dt_string}.zip"

def compressFile(folder_name):
    print(folder_name)
    zipPW = getpass("Enter password ")
    with ZipFile(zip_file_location, "w") as zf:
        for root,dirs,files in os.walk(folder_name):
            for filed in files:
                zf.write(f"{root}/{filed}", compress_type=ZIP_DEFLATED)
        zf.setpassword(bytes(zipPW, "UTF-8"))
        zf.close()

