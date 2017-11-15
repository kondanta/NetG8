import nmap
import os
import re
from . import utils as utilities


def router_detection():
    lst = list()
    ip_table = list()
    os_list = list()

    nm = nmap.PortScanner()

    a = utilities.get_neigh()
    print(a)
    b = re.compile(r"(.*)(?: dev.*)")
    c = (b.findall(a))
    print(c)

    for ip in c:
        a = nm.scan(ip, arguments="-d -d")
        if nm[ip]['tcp'][179]['state'] == "open": # bgp
            f = open('wall.dat', 'a')
	      	x = "I found Router: %s" %(ip)
	      	f.write(x)
            f.close()
        elif nm[ip]['tcp'][2042]['state'] == "open":
        	f = open('wall.dat', 'a')
	      	x = "I found Router: %s" %(ip)
	      	f.write(x)
            f.close()