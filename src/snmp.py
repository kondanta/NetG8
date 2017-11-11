import nmap
import os
import re
import utils as utilities

def snmp_port():
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
        if nm[ip]['tcp'][22]['state'] == "open":
            b = (a['scan'][ip]['tcp'])
            f = open('snmp.dat', 'a')
            f.write(ip+":\n")
            for key, values in b.items():
                x = "Port Number: %s, State: %s, Reason: %s, Service-name: %s. " %\
                (key, values['state'], values['reason'], values['name'])
                f.write(x+"\n")
            f.close()
