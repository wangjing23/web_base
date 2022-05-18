import os
import ipaddress
import subprocess

#Blank your screen
subprocess.call('clear', shell=True)

#Ask for input (xx.xx.xx.xx/xx)
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = ipaddress.ip_network(remoteServer, False)
#If strict is True and host bits are set in the supplied address, then ValueError is raised

for i in remoteServerIP.hosts():
    try:
        os.system("ping -c 1 {}".format(i))
        #"-c 1" means, ping one time, one ping only.
        print(i, "is active")
    except os.error:
        print("no response from ", i)
