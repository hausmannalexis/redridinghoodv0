import subprocess
import os
file_path = "misc/pumpkin.pulp"
if os.path.exists(file_path):
    subprocess.run(["sudo", "wifipumpkin3", "--pulp", file_path])
else:
    print(f"File '{file_path}' does not exist.")
