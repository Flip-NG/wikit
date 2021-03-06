#!/usr/bin/python3

import subprocess
import getpass
import os

user = getpass.getuser()

if user == 'root':
    pass

else:
    print("Must run script as root")
    exit()

print('Installing')

file = open("log.txt", "w+")
subprocess.call("pip install -r requirements.txt", shell=True, stdout=file)
file.close()

os.system('clear')

text = "#!/bin/bash \n cd $HOME/wiki/ && python3 ./wikit.py"

with open("/usr/local/bin/wikit", "w+") as f:
    f.write(text)

files = ["/usr/local/bin/wiki", "wikit.py"]

for i in files:
    subprocess.call(["sudo", "chmod", "+x", i])

os.remove("log.txt")

print('DONE')
exit()
