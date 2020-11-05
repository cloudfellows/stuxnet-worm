#/usr/bin/python
from pexpect import pxssh
s = pxssh.pxssh()
if not s.login(‘target.com’, ‘username’, ‘password’):
    print “Login Failed”
else:
    print “Logged in Successfully”
    s.sendline(raw_input(“Enter the Command: “))
    s.prompt()
    print s.before    # Print the Output
    s.logout()

    
# Read rock you file
# Store into variable .read
# use SSH session
# create a continous loop (for)
# login success or rock you PW was not meet
# Except try and accept phrase thgat keeps continuing regardless of errors
# Upon connection reveal password (open Ubuntu VM to see progress success/fail)