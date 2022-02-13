import os
from time import *
import sys
from turtle import color
from colorama import *

banner = """
██████╗  ██████╗██╗  ██╗
██╔══██╗██╔════╝╚██╗██╔╝
██████╔╝██║      ╚███╔╝ 
██╔═══╝ ██║      ██╔██╗ 
██║     ╚██████╗██╔╝ ██╗
╚═╝      ╚═════╝╚═╝  ╚═╝
"""
print(Fore.RED + banner)
print(Fore.BLUE+"[1] VPN                 [2] DDoS")
print(Fore.BLUE+"[3] PING                [4] SCAN DNS")
print(Fore.BLUE+"[5] PASSWORD GEN        [6] INFO")
print(Fore.BLUE+"[7] WHAT IS MY IP       [8] ETHERNET HARWESTER")
print(Fore.BLUE+"[9] PETYA CREATOR       [10] RANSOMWARE CREATOR")
print(Fore.BLUE+"[11] KEYLOGGER CREATOR  [12] CRYPT   ")
while True: 
    sec = input("root@27.158.89.111~# ")
    if sec=="1":
        os.system("start vpn.exe")
    elif sec=="2":
        ip = input("Enter a ip = ")
        os.system("python hammer.py -p 80 -s "+ip)
    elif sec=="3":
        os.system("start connect.bat")
    elif sec=="4":
        os.system("start scan.bat")        
    elif sec=="5":
        os.system("start pass.bat")
    elif sec=="6":
        os.system("start info.bat")
    elif sec=="7":
        os.system("start https://www.whatismyip.org")  
    elif sec=="8":
        os.system("python harvest.py")
    elif sec=="9":
        os.system("start builder_petya.exe")
    elif sec=="10":
        os.system("start builder_chaos.exe")
    elif sec=="11":
        os.system("start builder_hakops.exe")
    elif sec=="12":
        os.system("start crypter.exe")

    else:
        print("Wrong Command")
