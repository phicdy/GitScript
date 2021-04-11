import subprocess
from subprocess import PIPE

proc2 = subprocess.run('git branch | peco', shell=True,  stdout=PIPE, stderr=PIPE, text=True)
selected = proc2.stdout

selected_branch = proc2.stdout.strip()

proc_checkout = subprocess.run('git checkout ' + selected_branch, shell=True,  stdout=PIPE, stderr=PIPE, text=True)
print("Switched to branch '" + selected_branch + "'")

