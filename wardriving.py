import os
import subprocess
import sys
import urllib.request
import random
from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
networks_file_path = os.path.join(downloads_path, "networks.txt")
bssids_file_path = os.path.join(downloads_path, "bssids.txt")
mac_vendor_file_path = os.path.join(downloads_path, "mac-vendor.txt")
os.makedirs(downloads_path, exist_ok=True)
def install_package(package):
    subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
def download_mac_vendor_file():
    url = "https://raw.githubusercontent.com/aallan/README/master/mac-vendor.txt"
    destination = mac_vendor_file_path
    if not os.path.exists(destination):
        try:
            print(f"Downloading MAC vendor file from {url}")
            urllib.request.urlretrieve(url, destination)
            print(f"Downloaded MAC vendor file to {destination}")
        except Exception as e:
            print(f"Error downloading MAC vendor file: {e}")
    else:
        print("MAC vendor file already exists.")
required_packages = ["scapy"]
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install_package(package)
def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode
def check_interface(interface):
    if run_command(["sudo", "ifconfig", interface]) != 0:
        print(f"Error: Interface {interface} does not exist.")
        sys.exit(1)
    print(f"Interface {interface} is valid.")
def set_monitor_mode(interface):
    try:
        run_command(["sudo", "ifconfig", interface, "down"])
        run_command(["sudo", "macchanger", "-r", interface])
        run_command(["sudo", "iwconfig", interface, "mode", "monitor"])
        run_command(["sudo", "ifconfig", interface, "up"])
    except subprocess.CalledProcessError as e:
        print(f"Error setting monitor mode: {e}")
        sys.exit(1)
def set_channel(interface, channel):
    try:
        run_command(["sudo", "iwconfig", interface, "channel", str(channel)])
    except subprocess.CalledProcessError as e:
        print(f"Error setting channel: {e}")
def resolve_vendor(bssid):
    mac_prefixes = {}
    try:
        with open(mac_vendor_file_path) as f:
            for line in f:
                if line.strip():
                    parts = line.split("\t")
                    if len(parts) == 2:
                        mac_prefix = parts[0].strip().upper()[:6]
                        vendor = parts[1].strip()
                        mac_prefixes[mac_prefix] = vendor
                    else:
                        print("Invalid line format in mac-vendor.txt:", line)
    except Exception as e:
        print("Error reading mac-vendor.txt file:", e)
    bssid_clean = bssid.replace(':', '').upper()
    prefix = bssid_clean[:6]
    vendor = mac_prefixes.get(prefix, "Unknown")
    return vendor
def process_packet(packet, discovered_networks):
    try:
        if packet.haslayer(Dot11Beacon):
            bssid = packet.addr3
            ssid = packet.info.decode()
            if bssid not in [network['BSSID'] for network in discovered_networks]:
                vendor = resolve_vendor(bssid)
                discovered_networks.append({"BSSID": bssid, "SSID": ssid, "Vendor": vendor})
                print_networks(discovered_networks)
                save_to_file(discovered_networks)
    except Exception as e:
        print(f"Error processing packet: {e}")
def scan_channel(interface, discovered_networks):
    try:
        channel = random.randint(1, 13)
        set_channel(interface, channel)
        sniff(iface=interface, prn=lambda pkt: process_packet(pkt, discovered_networks), store=0, timeout=0.5, count=1000)
    except Exception as e:
        print(f"Error during scanning: {e}")
def print_networks(discovered_networks):
    os.system('clear')
    print("{:<6} {:<20} {:<40} {:<40}".format("Count", "BSSID", "Vendor", "SSID"))
    print("-" * 106)
    if discovered_networks:
        for i, network in enumerate(discovered_networks, start=1):
            bssid = network.get('BSSID', 'Unknown')
            ssid = network.get('SSID', 'Unknown')
            vendor = network.get('Vendor', 'Unknown')
            print("{:<6} {:<20} {:<40} {:<40}".format(i, bssid, vendor, ssid))
    else:
        print("No networks discovered yet.")
    print("-" * 106)
def save_to_file(discovered_networks):
    try:
        with open(networks_file_path, 'w') as f:
            for network in discovered_networks:
                f.write("{:<20} {:<40} {:<40}\n".format(network.get('BSSID', 'Unknown'), network.get('Vendor', 'Unknown'), network.get('SSID', 'Unknown')))

        with open(bssids_file_path, 'w') as f:
            for network in discovered_networks:
                f.write("{}\n".format(network.get('BSSID', 'Unknown')))
    except OSError as e:
        print(f"Error saving to file: {e}")
if __name__ == "__main__":
    interface = "wlan0"  # You can change this or make it a command-line argument
    check_interface(interface)
    set_monitor_mode(interface)
    download_mac_vendor_file()
    discovered_networks = []
    try:
        while True:
            scan_channel(interface, discovered_networks)
            save_to_file(discovered_networks)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        save_to_file(discovered_networks)
