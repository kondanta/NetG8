from scapy.all import *

def smpl_callback(pkt):
    print(pkt.summary())

def dtl_callback(pkt):
    pkt.show()

def srdst_callback(pkt):
        print("Source: {} --> Destination: {}".format(pkt[IP].src, pkt[IP].dst))

def srdstport_callback(pkt):
    print("Source: {}:{} --> Destination: {}:{}".format(pkt[IP].src, pkt[IP].sport, pkt[IP].dst, pkt[IP].dport))

def sdindex_callback(pkt):
    if pkt[TCP].payload:
        print("\nSource:{} Destination:{}:{} Index:\n{}".format(pkt[IP].src, pkt[IP].dst, pkt[IP].dport, str(bytes(pkt[TCP].payload))))

def test_callback(pkt):
    if pkt[TCP].payload:
        if pkt[IP].dport == 80:
            print("\nSource:{} Destination:{}:{} Index:\n{}".format(pkt[IP].src, pkt[IP].dst, pkt[IP].dport, str(bytes(pkt[TCP].payload))))

menu = """
Menu:
1-) Simplified output.
2-) Detailed output.
3-) Source-Destination mode.
4-) Source-Destination w/Ports mode.
5-) Src-Dst w/Index(TCP only) mode.
6-) Test Scan(Option 5 but only for port 80)
Q-) Exit
"""

def sniffer():
    while True:
        try:
            print(menu)
            x = input("Please select an option > ")

            if x == '1':
                sniff(prn=smpl_callback, store=0)

            elif x == '2':
                sniff(prn=dtl_callback, store=0)

            elif x == '3':
                sniff(filter="ip", prn=srdst_callback, store=0)

            elif x == '4':
                sniff(filter="ip", prn=srdstport_callback, store=0)

            elif x == '5':
                sniff(filter="tcp", prn=sdindex_callback, store=0)

            elif x == '6':
                sniff(filter="tcp", prn=test_callback, store=0)

            elif x == str.lower('Q'):
                sys.exit(1)

            else:
                print("[*] Invalid option.")
                
        except KeyboardInterrupt:
            print("!!! User requested exit operation.")
            return


