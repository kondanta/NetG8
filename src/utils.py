from scapy.all import *
import os
"""
This file contains utility functions of the program that needs externally.
"""
conf.L3socket = L3RawSocket
TIMEOUT = 2
conf.verb = 0

def get_nmap(ip, option=''):
	# default nmap scan for open ports!
	command = "nmap " + option + " -oG" + " " + "-" + " " + ip
	process = os.popen(command)
	return str(process.read())


def validate(name='icmp.dat'):
	"""
	Checks the IPs in the given @name file are alive.
	"""
	lst = list()
	validated_ips = list()

	# If icmp.dat file has nothing to pass, we should first collect to IPs.
	if os.stat(name).st_size == 0:
		print("No IPs found in 'icmp.dat'. [*] Returning to the Main Menu!")
		return

	for ips in open(name, "r").readlines():
		lst.append(ips.strip())

	for ip in lst: # some bs
		packet = IP(dst=ip, ttl=20)/ICMP()
		reply = sr1(packet, timeout=TIMEOUT)
		if not (reply is None):
			validated_ips.append(reply.src)
	
	os.remove("icmp.dat") 
			
	f = open("icmp.dat", "w")
	for i in validated_ips:
		print(i)  # should we continue to print online ip's on console ?
		f.write(i + '\n')
	f.close()


# I don't like this, should be improved!.
def help_menu(fucntionname):
	if fucntionname == "PING":
		print("Ping Usage: You should provide two distinc ip adresses to scaning range. \n\
			Or It'll scan the defualt ip range: 192.168.1.1 - 192.168.1.255")
	elif fucntionname == "PORT SCAN":
		print("Port Scan Usage: Be sure icmp.dat file is available and not empty.")
	elif fucntionname == "MAN":
		x = """
		=========================================================================
		[*] Ping Usage: You should provide two distinc ip adresses to scaning range.\n
			Or It'll scan the defualt ip range: 192.168.1.1 - 192.168.1.255"
		[*] Port Scan Usage: Be sure icmp.dat file is available and not empty.
		=========================================================================
		"""
		print(x)
	else:
		print("The function you're trying to reach is not implemented.")