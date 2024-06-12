import subprocess
choice=input("1. domain or 2. username? ")
if choice == "domain" or choice == "1":
  email=input("enter email: ")
  subprocess.run(["sudo", "pwned", "searched", email])
elif choice=="2" or choice=="username":
  user=input("enter user: ")
  subprocess.run(["sudo", "pwned", "searched", user])
