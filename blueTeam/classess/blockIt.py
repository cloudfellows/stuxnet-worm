import subprocess,sys,os
import win32com.shell.shell as shell


## function to add firewall rule to block ports
def add_rule(rule_name, port):
    subprocess.Popen(f"powershell.exe New-NetFirewallRule -DisplayName '{rule_name}' -Profile @('Domain', 'Private') -Direction Inbound -Action Block -Protocol TCP -LocalPort @('{port}')", shell = False)
    print(f"Rule {rule_name} for {port} added")
