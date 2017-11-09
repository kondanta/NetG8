from scapy.all import *
from src.utils import get_nmap
import os
import re


conf.L3socket = L3RawSocket
TIMEOUT = 2
conf.verb = 0



def icmp_ping(ip1='192.168.1.1', ip2='192.168.1.255'):
	"""
	Takes two IP addresses as a paramters to find pinging range.
	"""
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
	"""
	Uses nmap to scan alive hosts ports.
	For ip's icmp.dat file is required.
	"""
	lst = list()
	ip_list = list()
	port_list = list()

	for ips in open("icmp.dat", "r").readlines():
		lst.append(ips.strip())

	for ip in lst:
		try:
			scan_result = get_nmap(ip, "-d -d ")
			scan_result = scan_result.replace("\n", "")

			prt = re.compile(r'(?:.*Ports:\s)(.*)#.*')
			ip_list = (prt.findall(scan_result))
			print(ip_list)
			# if regex returns nothing, We have no ports available/open.
			if not ip_list:
				ip_list = ["None"]

			for item in ip_list:
				item = item.replace('/'," ")
				port_list.append(item)

			for index, item in enumerate(port_list):
				port_list[index] = item

		except Exception as e:
			print("Port Managing Error: %s" % e)
			pass
		
	try:
		"""
		It will write the ports.dat file as follows:
		Host's Ip address, Port number, Port Status[open, restricted], type[tcp/udp], service-name
		"""
		# FIXME: It doesnt write the IPs that has no OpenPorts.
		f = open('ports.dat', 'a')
		cnt = 0
		
		for i in port_list:
			f.write(lst[cnt]+", ")
			# for j in i:
			f.write(i) 
			cnt += 1
			f.write('\n')

		f.close()
		print("[*] Ports.dat is created!\n")
	except Exception as e:
		print("File Writing Error: %s " % e)


def open_port_identification():
	lst = list()
	ip_list = list()
	ip_table = list()
	port_list = list()

	for ips in open("ports.dat", "r").readlines():
		lst.append(ips.strip())

	for item in lst:
		item = item.split(",")
		ip_list.append(item[0])
		ip_table.append(item[0])

	print(ip_list)
	for ip in ip_list:
		try:
			scan_result = get_nmap(ip)
			scan_result = scan_result.replace("\n", "")

			prt = re.compile(r'(?:.*Ports:\s)(.*)(?:\S\t)(?:Ignored.*)')
			ip_list = (prt.findall(scan_result))
			# if regex returns nothing, We have no ports available/open.
			if not ip_list:
				ip_list = ["None"]

			for item in ip_list:
				item = item.replace('/'," ")
				port_list.append(item)

			for index, item in enumerate(port_list):
				port_list[index] = item

		except Exception as e:
			print("Port Managing Error: %s" % e)
			pass
	try:
		"""
		It will write the ports.dat file as follows:
		Host's Ip address, Port number, Port Status[open, restricted], type[tcp/udp], service-name
		"""
		# FIXME: It doesnt write the IPs that has no OpenPorts.
		f = open('open_ports.dat', 'a')
		ctr = 0
		print(port_list)
		for i in port_list:
			if i == "None":
				continue
			else:
				f.write(ip_table[ctr]+" ,")
				f.write(i) 
				ctr += 1
			f.write('\n')

		f.close()
		print("[*] OpenPorts.dat is created!\n")
	except Exception as e:
		print("File Writing Error: %s " % e)

  