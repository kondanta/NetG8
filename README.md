### Network Scanner
It's a simple network scanner that scans network, finds open ports throught this ports find the Operating systems
of the found ips. Also do Syn flood attack as well as the network sniff. It's actually a tool that merges some
good features from different tools available.

### Dependencies 
So let me briefly explain the dependencies. It requires nmap and scapy installed through python package manager.
`pip install > requirements.txt`
Also one function requires unix operating system for run.

### Functions and Usages
Since program has simple UI, it wouldn't be a problem to figure out how it does things.
However; There are some restrictions I'd like to mention.
- First of all you `SHOULD` use first 4 functions with an order. They all depends eachother's results.
- Finding OSs and Routers are not compatible with Windows OS yet.
- Syn Flood Attack automatically triggers the tcpdump. That's why `I assume that you already have that. `
- Sniff function does sniff the local network (as you can guess from the name) and prints the result. However there are several options you can choose among them. I believe sniff menu is self-explanatory.


### Installation
Just clone/download the repository and run the main.py.
`It'll require super user permissions to run sucessfully`. Without sudo, you can do basic scans though.