import sys
if sys.version_info[0] < 3:
	raise SystemError("Please run this program with Python 3!")
import src.icmp as icmp
import src.utils as utilities

menu = """
Menu:
1-) PING
2-) PORT SCAN
3-) OPEN PORT SCAN
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
				print("no icmp.dat file")
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
		elif x == "--help":
			inp = input("[*] Type the function name you'd like to see Instructions.\n Use --help man for Detailed Explanation.\
				> ")

			utilities.help_menu(str.upper(inp))
		elif x == str.lower('Q'):
			sys.exit(1)
		else:
			print("[*] Wrong Usage. Please --help to See Detailed Explanation of Functions")
	except KeyboardInterrupt:
		print("!!! User requested exit operation.")
		sys.exit(1)