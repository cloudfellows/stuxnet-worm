import subprocess,sys,os
import win32com.shell.shell as shell

## Ading rule to allow the ports
def add_rule_allow(port):
    rule = f"Get-NetFirewallRule -DisplayName 'Block {port}' | Remove-NetFirewallRule"
    p = subprocess.Popen(f"powershell.exe {rule}", shell = False, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) 
    p.communicate()
    subprocess.Popen(f"powershell.exe New-NetFirewallRule -DisplayName 'Allow {port}' -Profile @('Domain', 'Private', 'Public') -Direction Inbound -Action Allow -Protocol TCP -LocalPort @('{port}')", shell = False, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    print(f"Rule for allowing port {port} added")
