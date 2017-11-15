import sys

menu = """
Menu:
1-) Icmp file.
2-) Ports file.
3-) Open Ports file.
4-) OS file.
5-) Router/Firewall file.
6-) Web server file.
7-) SNMP file.
Q-) Exit
"""

def show():
    while True:
        try:
            print(menu)
            x = input("Please select an option > ")

            if x == '1':
                f = open('./icmp.dat', 'r')
                file_contents = f.read()
                print (file_contents)
                f.close()
                input("Press any key to continue.")
            
            elif x == '2':
                f = open('./ports.dat', 'r')
                file_contents = f.read()
                print (file_contents)
                f.close()
                input("Press any key to continue.")

            elif x == '3':
                f = open('./open_ports.dat', 'r')
                file_contents = f.read()
                print (file_contents)
                f.close()
                input("Press any key to continue.")

            elif x == '4':
                f = open('./os_ident.dat', 'r')
                file_contents = f.read()
                print (file_contents)
                f.close()
                input("Press any key to continue.")

            elif x == '5':
                f = open('./wall.dat', 'r')
                file_contents = f.read()
                print (file_contents)
                f.close()
                input("Press any key to continue.")

            elif x == '6':
                f = open('./web.dat', 'r')
                file_contents = f.read()
                print (file_contents)
                f.close()
                input("Press any key to continue.")

            elif x == '7':
                f = open('./snmp.dat', 'r')
                file_contents = f.read()
                print (file_contents)
                f.close()
                input("Press any key to continue.")

            elif x == str.lower('Q'):
                return

            else:
                print("[*] Invalid option.")

        except KeyboardInterrupt:
            print("!!! User requested exit operation.")
            return
        except FileNotFoundError:
            print("File is not found. Please run the function first.")
            return