from scapy.all import *
import socket
import os
import re


conf.L3socket = L3RawSocket

TIMEOUT = 2
conf.verb = 0


def icmp_ping(ip1='192.168.1.1', ip2='192.168.1.255'):
	try:
		i1 = ip1.split(".")
		i2 = ip2.split(".")
		ip = i1[:3]
		ip_o = ".".join(ip) + "."
		for ip in range(int(i1[3]), int(i2[3])+1): # some bs
			packet = IP(dst=ip_o + str(ip), ttl=20)/ICMP()
			reply = sr1(packet, timeout=TIMEOUT)
			if not (reply is None):
				f = open('icmp.dat', 'a')
				f.write(reply.src + '\n')
				f.close()
				x = reply.src + " is online"
				print(x)
			else:
				x = "Timeout waiting for %s" % packet[IP].dst
				print(x)
	except OSError:
		print("Check the given ips")
	

def port_identification():
	lst = list()
	ip_list = list()
	port_list = list()

	test = list()



	for ips in open("../icmp.dat", "r").readlines():
		lst.append(ips.strip())

	# Validation of the IP adresses.
	for ip in lst:
		try:
			# regexp: [0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*$
			socket.inet_aton(ip) # legal. But need to check if the ip is alive !
		except Exception as e: # illegal
			print("Due to the illegal Ip existence, program is exiting. Please check out the ip addresses\
				in the 'icmp.dat' file.")
			return
	

	# Prepearing the nmap
	def get_nmap(options='-F', ip=ip):
		command = "nmap " + options + " " + "-oG" + " " + "-" + " " + ip
		process = os.popen(command)
		return str(process.read())


	a = get_nmap('-F' , 'scanme.nmap.org')
	a = a.replace("\n", "")

	file = open("nmap_parse.dat", 'w+')
	file.write(a)
	file.close()

	# Regex....
	prt = re.compile(r'(?:.*Ports:\s)(.*)(?:\S\t)(?:Ignored.*)')
	
	for line in open('nmap_parse.dat'):
		ip_list = (prt.findall(line))
	
	ip_list = ip_list[0].split(",")

	for item in ip_list:
		item = item.replace('/'," ")
		port_list.append(item)


	for index, item in enumerate(port_list):
		item = item.split()
		port_list[index] = item

	# print(port_list)

	# for iteml, itemp in lst, port_list:
	# 	item = item + port_list
	# 	test.append(item)

	wr = [j for i in zip(lst,port_list) for j in i]

	print(flat)


port_identification()
