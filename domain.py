import subprocess
domain=input("domain?: ")
question=input("do you want to start with whatweb? yes or no: ")
if question=="yes" or question=="y":
  subprocess.run(["sudo", "whatweb", domain])
else:
  pass
question_dnsrecon=input("do you want to continue with dnsrecon? yes or no: ")
if question_dnsrecon == "yes" or question_dnsrecon == "y":
  subprocess.run(["sudo", "dnsrecon", "-d", domain])
else:
  pass
question_dnsrecon2=input("do you want to continue with dnsenum? yes or no: ")
if question_dnsrecon2 == "yes" or question_dnsrecon2 == "y":
  subprocess.run(["sudo", "dnsenum", domain])
else:
  pass
question_dnsrecon4=input("do you want to continue with theHarvester? yes or no: ")
if question_dnsrecon4 == "yes" or question_dnsrecon4 == "y":
  subprocess.run(["sudo", "theHarvester", "-d", domain])
else:
  pass
question_dnsrecon5=input("do you want to continue with wapiti? yes or no: ")
if question_dnsrecon5 == "yes" or question_dnsrecon5 == "y":
  subprocess.run(["sudo", "wapiti", "-u", domain])
else:
  pass
question_dnsrecon6=input("do you want to continue with sqlmap? yes or no: ")
if question_dnsrecon6 == "yes" or question_dnsrecon6 == "y":
  subprocess.run(["sudo", "sqlmap", "-u", domain, "-a", "--forms", "--crawl=2"])
else:
  pass
question_dnsrecon7=input("do you want to continue with dnsenum? yes or no: ")
if question_dnsrecon7 == "yes" or question_dnsrecon7 == "y":
  subprocess.run(["sudo", "commix", "-u", domain, "--crawl=2"])
else:
  pass
