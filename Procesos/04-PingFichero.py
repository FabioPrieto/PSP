import subprocess

with open("salidaPing.txt","w") as f:
    try:
        subprocess.run(["ping", "google.com","-n","5"], stdout=f)
    except subprocess.CalledProcessError as e:
        print(e.output)