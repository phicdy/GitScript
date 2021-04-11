import subprocess
from subprocess import PIPE

# For when last commit is selected, print +1 commit
proc = subprocess.run('git log -16 --pretty=format:"%h %s %d"', shell=True,  stdout=PIPE, stderr=PIPE, text=True)
lines = proc.stdout.split("\n")

proc2 = subprocess.run('git log -15 --pretty=format:"%h %s %d" | peco', shell=True,  stdout=PIPE, stderr=PIPE, text=True)
selected = proc2.stdout
print(selected)

selected_commit = proc2.stdout.split()[0]

for i, line in enumerate(lines):
    if line.split()[0] == selected_commit:
        selected_previous_commit = lines[i+1].split()[0]
        break

proc_file = subprocess.run('git diff ' + selected_previous_commit + '..' + selected_commit + ' --name-only | peco', shell=True,  stdout=PIPE, stderr=PIPE, text=True)
selected_file = proc_file.stdout
print(selected_file)


proc_selected_file_diff = subprocess.run('git diff ' + selected_previous_commit + '..' + selected_commit + ' -- ' + selected_file, shell=True,  stdout=PIPE, stderr=PIPE, text=True)

lines_diff = proc_selected_file_diff.stdout.split("\n")
for line in lines_diff:
    if line.startswith("+"):
        # green
        print('\033[32m' + line + '\033[0m')
    elif line.startswith("-"):
        # red
        print('\033[31m' + line + '\033[0m')
    else:
        print(line)
