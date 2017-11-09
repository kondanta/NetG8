import os
"""
This file contains utility functions of the program that needs externally.
"""

def get_nmap(ip):
	# default nmap scan for open ports!
	command = "nmap " + "-oG" + " " + "-" + " " + ip
	process = os.popen(command)
	return str(process.read())