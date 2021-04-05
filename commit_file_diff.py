import subprocess
from subprocess import PIPE

proc = subprocess.run('git log -3 --pretty=format:"%h %s"', shell=True,  stdout=PIPE, stderr=PIPE, text=True)
print(proc.stdout)

lines = proc.stdout.split("\n")

input_commit_index = input("\nEnter commit index\n")
selected_commit = lines[int(input_commit_index)].split()[0]
selected_previous_commit = lines[int(input_commit_index)+1].split()[0]

proc_diff = subprocess.run('git diff ' + selected_commit + ' --name-only', shell=True,  stdout=PIPE, stderr=PIPE, text=True)
print("\nFiles:")
print(proc_diff.stdout)

line_files = proc_diff.stdout.split("\n")

input_file = input("Enter file index\n")
selected_file = line_files[int(input_file)].split()[0]
print(selected_file)

proc_selected_file_diff = subprocess.run('git diff ' + selected_previous_commit + '..' + selected_commit + ' -- ' + selected_file, shell=True,  stdout=PIPE, stderr=PIPE, text=True)
print(proc_selected_file_diff.stdout)
