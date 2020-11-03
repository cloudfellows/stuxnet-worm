import subprocess,sys,os
import win32com.shell.shell as shell

# ASADMIN = 'asadmin'
# if sys.argv[-1] != ASADMIN:
#     script = os.path.abspath(sys.argv[0])
#     params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
#     shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
#     sys.exit(0)
# print ("I am root now.")

def add_rule(rule_name, port):
    subprocess.Popen(f"powershell.exe New-NetFirewallRule -DisplayName '{rule_name}' -Profile @('Domain', 'Private') -Direction Inbound -Action Allow -Protocol TCP -LocalPort @('{port}')", shell = False) 
    print(f"Rule {rule_name} for {port} added")
title = input("What is the title of the rule? ")
port_number = input("What port would you like to open? ")
add_rule(title, int(port_number))