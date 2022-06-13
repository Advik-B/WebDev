import subprocess

subprocess.run('powershell Stop-Service -Name "Host Network Service"', shell=True)
subprocess.run('C:\Windows\system32\svchost.exe -k NetSvcs -p', shell=True)
