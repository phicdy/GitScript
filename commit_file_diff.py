import subprocess
from subprocess import PIPE

proc = subprocess.run('git log -15 --pretty=format:"%h %s %d"', shell=True,  stdout=PIPE, stderr=PIPE, text=True)
lines = proc.stdout.split("\n")
[print(str(i) + ") " + commit) for i, commit in enumerate(lines)]

input_commit_index = input("\nEnter commit index\n")
selected_commit = lines[int(input_commit_index)].split()[0]
selected_previous_commit = lines[int(input_commit_index)+1].split()[0]

proc_diff = subprocess.run('git diff ' + selected_previous_commit + '..' + selected_commit + ' --name-only', shell=True,  stdout=PIPE, stderr=PIPE, text=True)
line_files = proc_diff.stdout.strip().split("\n")

print("\nFiles:")
[print(str(i) + ") " + file) for i, file in enumerate(line_files)]

input_file = input("\nEnter file index\n")
selected_file = line_files[int(input_file)].split()[0]
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
