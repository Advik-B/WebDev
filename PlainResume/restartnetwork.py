import subprocess

subprocess.run('taskkill /f /im svchost.exe', shell=True)
subprocess.run('C:\Windows\system32\svchost.exe -k NetSvcs -p', shell=True)
