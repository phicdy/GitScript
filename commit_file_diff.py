import subprocess
from subprocess import PIPE

proc = subprocess.run('git log -3 --pretty=format:"%h %s"', shell=True,  stdout=PIPE, stderr=PIPE, text=True)
print(proc.stdout.split())
print(type(proc.stdout.split()))