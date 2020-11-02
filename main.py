from time import sleep
import socket,sys
from cryptography.fernet import Fernet
from classes.encrypt import *
keyLocation = "./key.key"
# display interface
def interface(keys):
    print("""
    Logo goes here
    1) Encrypt Folder & Zip
    2) Decrypt Folder & Zip
    3) Open port
    4) Close port
    5) Exit
    """)
    userInput = input("Enter your choice... ")
    if(userInput == "1"):
        ## encryption method
        userFolder=input("What folder do you want to input ")
        userFolder=f"./{userFolder}"
        encrptFolder(userFolder, keys)
    # elif(userInput == "2"):
    #     ## Decryption method
    # elif(userInput == "3"):-
    #     ## Open the port
    # elif(userInput == "4"):
    #     ## close the port
        # check_Port()
    else:
        ## exit
        print("Exiting...")
        sleep(1)
        exit()
# getting the key
def get_key():
    return open(keyLocation, "rb").read()
# creating the key 
def generate_key():
    key = Fernet.generate_key()
    with open(keyLocation, "wb") as key_file:
        key_file.write(key)
# Zip the folder
# Unzip
def main():
    ## creating the key
    generate_key()
    ## Get the key
    key=get_key()
    while True:
        interface(key)
if __name__ == "__main__":
    main()