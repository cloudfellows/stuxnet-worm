import subprocess,sys,os
import win32com.shell.shell as shell


## function to add firewall rule to block ports
def add_rule(port):
    rule = f"Get-NetFirewallRule -DisplayName 'Allow {port}' | Remove-NetFirewallRule"
    p = subprocess.Popen(f"powershell.exe {rule}", shell = False, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) 
    p.communicate()
    subprocess.Popen(f"powershell.exe New-NetFirewallRule -DisplayName 'Block {port}' -Profile @('Domain', 'Private', 'Public') -Direction Inbound -Action Block -Protocol TCP -LocalPort @('{port}')", shell = False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Rule for blocking port {port} added")
