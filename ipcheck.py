import subprocess
target=input("ip?: ")
subprocess.run(["sudo", "ping", "-c", "5", target])
subprocess.run(["sudo", "traceroute", target])
subprocess.run(["sudo", "nmap", "-sSCV", "-F", target])
