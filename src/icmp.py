from scapy.all import *
import os
import re
import socket


conf.L3socket = L3RawSocket

TIMEOUT = 2
conf.verb = 0


def icmp_ping(ip1='192.168.160.70', ip2='192.168.160.74'):
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
	a = ''

	for ips in open("icmp.dat", "r").readlines():
		lst.append(ips.strip())

	# print(lst)
	

	# Validation of the IP adresses.
	for ip in lst:
		try:
			socket.inet_aton(ip) # legal. But need to check if the ip is alive !

			def get_nmap(options='-F', ip=ip):
				command = "nmap " + options + " " + "-oG" + " " + "-" + " " + ip
				process = os.popen(command)
				return str(process.read())

			# regexp: [0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*$
			a = get_nmap('-p- -sT -sU' , ip)
			a = a.replace("\n", "")
		except Exception as e: # illegal
			# print("Due to the illegal Ip existence, program is exiting. Please check out the ip addresses\
				# in the 'icmp.dat' file.")
			print(e)
			return

	# a = get_nmap('-sT' , '192.168.171.22')
	# a = a.replace("\n", "")

	file = open("nmap_parse.dat", 'w+')
	file.write(a)
	file.close()

	# Regex....
	prt = re.compile(r'(?:.*Ports:\s)(.*)(?:\S\t)(?:Ignored.*)')
	
	for line in open('nmap_parse.dat'):
		ip_list = (prt.findall(line))

	try:
		ip_list = ip_list[0].split(",")
	except IndexError:
		print("I could not find any ports... ,__,")

	for item in ip_list:
		item = item.replace('/'," ")
		port_list.append(item)


	for index, item in enumerate(port_list):
		item = item.split()
		port_list[index] = item


	try:
		f = open('test.dat', 'w')
		cnt = 0
		for i in port_list:
			f.write(lst[cnt]+" ")
			for j in i:
				f.write(j+" ") # what if 4 ports are open ?
			# cnt += 1
			f.write('\n')

		f.close()
	except IndexError:
		print("Something happened ... ,____,")


def validate(name='icmp.dat'):
	lst = list()
	validated_ips = list()

	for ips in open(name, "r").readlines():
		lst.append(ips.strip())


	print(lst)
	for ip in lst: # some bs
		packet = IP(dst=ip, ttl=20)/ICMP()
		reply = sr1(packet, timeout=TIMEOUT)
		if not (reply is None):
			validated_ips.append(reply.src)
	
	os.remove("icmp.dat")
			
	f = open("icmp.dat", "w")
	for i in validated_ips:
		print(i)
		f.write(i + '\n')
	f.close()

