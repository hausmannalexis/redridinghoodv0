import subprocess
choice=input("1. username, 2. email & 3. phone number")
if choice=="1" or choice=="username":
  target=input("enter username: ")
  subprocess.run(["sudo", "sherlock", target])
  subprocess.run(["sudo", "userrecon", target])
  subprocess.run(["sudo", "whatsmyname", "-u", target])
else:
  pass
if choice=="2" or choice=="email":
  target=input("enter email: ")
  subprocess.run(["sudo", "holehe", target])
  subprocess.run(["sudo", "theHarvester", "-d", target, "-l", "500", "-b", "all"])
  subprocess.run(["sudo", "mailsniper", "--email", target])
else:
  pass
