import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # Surpress the scapy warning msg of ipv6. 
import sys
if sys.version_info[0] < 3:
	raise SystemError("Please run this program with Python 3!")
import src.icmp as icmp
import src.utils as utilities
import src.webserver as webserver
import src.snmp as snmp
import src.sniff as sniff
import src.show as show
import src.synattack as synattack

menu = """
Menu:
1-) ICMP PING
2-) PORT SCAN
3-) OPEN PORT SCAN
4-) OS IDENTIFICATION
6-) WEB SERVER DETECTION
7-) SNMP DETECTION
8-) SYN FLOOD ATTACK
9-) SHOW FILES
10-) SNIFF
Q-) Exit
"""

while True:
	try:
		print(menu)
		x = input("Please select a process > ")
		
		if x == '1':
			try:
				ip = input("Please provide the first ip > ")
				ip2 = input("Please provide the second ip > ")
				icmp.icmp_ping(ip, ip2)
			except IndexError:
				icmp.icmp_ping()

		elif x == '2':
			try:
				utilities.validate()
				icmp.port_identification()
			except FileNotFoundError:
				print("No icmp.dat file.")
				icmp.icmp_ping()
				icmp.port_identification()

		elif x == '3':
			try:
				utilities.validate()
				icmp.open_port_identification()
			except Exception as e:
				print(e)

		elif x == '4':
			try:
				utilities.validate()
				icmp.os_ident()
			except Exception as e:
				print(e)

		elif x == '6':
			try:
				inp = input('Please specify the usage of the Web server Detection.')
				if not inp:
					webserver.web_server()
				webserver.web_server(inp)
			except Exception as e:
				print(e)

		elif x == '7':
			try:
				snmp.snmp_port()
			except Exception as e:
				print(e)

		elif x == '8':
			try:
				synattack.syn_attack()
			except Exception as e:
				print(e)

		elif x == '9':
			try:
				show.show()
			except Exception as e:
				print(e)

		elif x == '10':
			try:
				sniff.sniffer()
			except Exception as e:
				print(e)

		elif x == "--help":
			utilities.help_menu()

		elif x == str.lower('Q'):
			sys.exit(1)

		else:
			print("[*] Wrong Usage. Please --help to see detailed explanation of functions")
	except KeyboardInterrupt:
		print("!!! User requested exit operation.")
		sys.exit(1)