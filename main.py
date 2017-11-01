import src.icmp as icmp

menu = """
	Menu:
	1-) PING
	2-) PORT SCAN
	"""
print(menu)
x = int(input("Please select a process > "))

if x == 1:
	try:
		ip = input("Please provide the first ip > ")
		ip2 = input("Please provide the second ip > ")
		icmp.icmp_ping(ip, ip2)
	except IndexError:
		icmp.icmp_ping()

elif x == 2:
	try:
		icmp.port_identification()
	except FileNotFoundError:
		print("no icmp.dat file")
		icmp.icmp_ping()
		icmp.port_identification()