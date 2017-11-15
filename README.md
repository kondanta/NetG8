# CE 340 Cryptography & Network Security Assignment 3

## Title: Building Simple Tools
## Defined by: Süleyman Kondakcı (Instructor) , http://homes.ieu.edu.tr/~skondakci/ 
## Date to delivery: 15.11.2017, 17:00
## Project members: Taylan Doğan, Ünal Muslu

### Dependencies
Python Dependencies:
	- Python 3+
	- nmap
	- scapy
System Dependencies:
	- Unix
	- tcpdump 

For the successfull run for this program, the dependencies that mentioned above are required. Installing python
dependencies with pip:
	- ```pip install modul-name```
Installing with easy_install:
	- ```easy_install modul-name```

### Run Time
Program does require a root user to be run successfully. If user is not root some of the functionalities may not
work how they supposed to.
Running the program with super user privlege, simply type `sudo` in front of the `python main.py`.

### Functionalities
You expected to select functionalities from the given menu.

- ICMP Ping:
	- Icmp ping requires two ip addresses within the same netmask to calculate the range of the ip addresses to be
	scanned. Ex: $ > 192.168.1.1 $ > 192.168.1.100
	If user does not provide any ip addresses, it'll automatically scan the range of 192.168.1.1, 192.168.1.255.
	After a successfull scan, it'll create "icmp.dat" file in hw3 folder.
	- `Warning!` You're expected to handle all of the .dat file contents by yourself. If you are not maintain them
	by hand, this function append the new IP addresses in the same file. That may cause inconviniace for the user in
	terms of the increase of the waiting time to scanning.

- Port Scan:
	- To run this function, `icmp.dat` should be exist. If not, It'll call the ICMP Ping function with default Ip
	range to create the file.
	- All of the IP's in `icmp.dat` file are validating before the action starts. The dead IPs will be purged from
	the file.
	- Function does not require any user input for finding ports or the port range. It'll automatically scan all of the ports (65024) and append them into `ports.dat` file. However, having lots of IP addresses may cause longer
	scan time.

- Open Port Scan:
	- To run this function, `ports.dat` file should be exist. If not, Function give an Exception message "ports.dat"
	is not found" and terminates itself.
	- Ip's will be gathered from the `ports.dat` file, and validated again. The dead IPs will be purged from the
	file.
	- Function does not require any user input for finding open ports. It'll automatically scan all of the ports
	(65024) but only open ports will be appended to `open_ports.dat` file.

- Operating System Identification:
	- To run this function, `open_ports.dat` file should be exist. If not, Function give an Exception message and
	terminates itself.
	- It'll create a file named `os_ident.dat` with IP addresses and respective identified operating system names.

- Web Server Detection:
	- This function does not require any other file to run.
	- Function can take a user argument ['all', 'open'].
		- all:
			Function will write all of the ports['closed','open'] into the `web.dat`
		- open:
			Function will write only open ports to `web.dat`
	- If user does not give any parameters, function will write only open ports into the file.

