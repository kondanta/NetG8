import nmap

def web_server(option='open'):
	# Predefined web-servers.
	host = ['www.eksisozluk.com', 'www.myanimelist.net', 'www.google.com.tr', 'www.yahoo.com.tr',
			'www.github.com', 'www.hotmail.com', 'www.twitter.com', 'www.facebok.com', 'www.devrant.com',
			'www.pearson.com']
	nm = nmap.PortScanner()
	
	try:
		for ip in host:
			if option == 'open':
				a = nm.scan(ip)
			elif option == 'all':
				a = nm.scan(ip, arguments="-d -d")
			else:
				print('[*] Wrong Usage!!! Please check the --help Menu')
				return

			b = a['scan']
			for key, value in b.items():
				x = "Address: %s, Protocol: TCP," % (key)
				for k1, v1 in value['tcp'].items():
					y = x + "Port: %s" % (k1)
					f = open('web.dat', 'a')
					f.write(y)
					f.write('\n')
					f.close()
			print("Scanning next IP[*]")
	except KeyboardInterrupt as e:
		print('[*] User requested to exit!')
