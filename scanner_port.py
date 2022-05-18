import socket
import subprocess
import threading
import concurrent.futures
import sys
from datetime import datetime

#Blank your screen
subprocess.call('clear', shell=True)

#Ask for input 
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#print a nice banner with information on which host we are about to scan
print("_" * 60)
print("Please wait, scanning remote host", remoteServer)
print("_" * 60)

#Check the data and time the scan was started
#t1 = datetime.now()

#thread
print_lock = threading.Lock()

#scan function
def scan(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    try:
        sock.connect((ip, port))
        sock.close()
        with print_lock:
            print("Port {}: open".format(port))
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

#Using the range function specify ports
#thread
with concurrent.futures.ThreadPoolExecutor() as executor:
    for port in range(1, 1000):
        executor.submit(scan, remoteServer, port)

#checking time again
#t2 = datetime.now()

#calculate the difference in time to know how long the scan look
#total = t2 - t1

#print the information on the screen
#print("scanning Completed in: ", total)










