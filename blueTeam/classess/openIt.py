import subprocess,sys,os
import win32com.shell.shell as shell

## Ading rule to allow the ports
def add_rule_allow(rule_name, port):
    subprocess.Popen(f"powershell.exe New-NetFirewallRule -DisplayName '{rule_name}' -Profile @('Domain', 'Private') -Direction Inbound -Action Allow -Protocol TCP -LocalPort @('{port}')", shell = False) 
    print(f"Rule {rule_name} for {port} added")
