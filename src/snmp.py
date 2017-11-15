import nmap
import os
import re
from . import utils as utilities

def snmp_port():
    lst = list()
    ip_table = list()
    os_list = list()

    nm = nmap.PortScanner()

    a = utilities.get_neigh()
    b = re.compile(r"(.*)(?: dev.*)")
    c = (b.findall(a))
    
    for ip in c:
        scan = nm.scan(ip, arguments="-d -d")
        if nm[ip]['tcp'][22]['state'] == "open":
            res = (scan['scan'][ip]['tcp'])
            f = open('snmp.dat', 'a')
            f.write(ip+":\n")
            for key, values in res.items():
                x = "Port Number: %s, State: %s, Reason: %s, Service-name: %s. " %\
                (key, values['state'], values['reason'], values['name'])
                f.write(x+"\n")
            f.close()
        else:
            print("There is no open SNMP port in scanned IP:{}".format(ip))

