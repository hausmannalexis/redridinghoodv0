import subprocess
subprocess.run(["sudo", "tput", "setaf", "2"])
subprocess.run(["sudo", "tput", "setab", "0"])
ask=input("do you want to reset the interface (y or n)?: ")
if ask == "y":
    subprocess.run(["sudo", "airmon-ng", "stop", "wlan0"])
    subprocess.run(["sudo", "airmon-ng", "stop", "wlan0mon"])
    subprocess.run(["sudo", "ip", "link", "set", "wlan0", "down"])
    subprocess.run(["sudo", "ifconfig", "wlan0", "up"])
    subprocess.run(["sudo", "dhclient", "wlan0"])
    subprocess.run(["clear"])
    pass
else:
    pass
subprocess.run(["clear"])
print("welcome to red riding hood\n")
print("     __o\n   _ \<_\n  (_)/(_)\n")
print("SLAVA UKRAINI!\n\n")
print("0. setup\n1. wifi crack\n2. fake ap\n3. wardriving\n4. ipcheck\n5. domain\n6. osint\n7. phish *blubb*\n\n")
choice = input("#?: ")
if choice == "0" or choice == "setup":
    subprocess.run(["sudo", "python3", "setup.py"])
elif choice == "1" or choice == "wlan crack":
    subprocess.run(["sudo", "python3", "wificrack.py"])
elif choice == "2" or choice == "fake ap":
    subprocess.run(["sudo", "python3", "pumpkin.py"])
elif choice == "3" or choice == "wardriving":
    subprocess.run(["sudo", "python3", "wardriving.py"])
elif choice == "4" or choice == "ipcheck":
    subprocess.run(["sudo", "python3", "ipcheck.py"])
elif choice == "5" or choice == "domain":
    subprocess.run(["sudo", "python3", "domain.py"])
elif choice == "6" or choice == "osint":
    subprocess.run(["sudo", "python3", "osint.py"])
elif choice == "7" or choice == "phish":
    subprocess.run(["sudo", "python3", "setoolkit.py"])
else:
    quit()
