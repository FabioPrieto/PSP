import subprocess

try:
    subprocess.run(['Notepad.exe'])
except subprocess.CalledProcessError as e:
    print(e.output)