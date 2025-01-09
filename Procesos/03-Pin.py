import subprocess

try:
    subprocess.run(["ping", "google.com","-n","5"])
except subprocess.CalledProcessError as e:
    print(e.output)