from scapy.all import *
import os
import subprocess as sub


"""
This file contains utility functions of the program that needs externally.
"""
conf.L3socket = L3RawSocket
TIMEOUT = 2
conf.verb = 0

def get_neigh(option=''):
	command = "ip " + "neigh " + option
	process = os.popen(command)
	return str(process.read())


def get_tcpdump(srcip):
	srctrack = "src host %s" % (srcip)
	p = sub.Popen(('sudo', 'tcpdump', '-l','-n', srctrack, '-vv'), stdout=sub.PIPE)
	for row in iter(p.stdout.readline, b''):
		print(row.rstrip())


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

def help_menu():
	print("Please check out the ReadMe for help.")