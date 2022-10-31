import subprocess


files = ["task_4_broker.py", "task_4_user.py"]
for file in files:
    subprocess.Popen(args=["start", "python", file], shell=True, stdout=subprocess.PIPE)