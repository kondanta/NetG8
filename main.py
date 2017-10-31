import src.icmp as icmp


x = int(input("Please select a process: "))

if x == 1:
	try:
		ip = input("Please provide the first ip")
		ip2 = input("Please provide the second ip")
		icmp.ICMPping(ip, ip2)
	except IndexError:
		icmp.ICMPping()