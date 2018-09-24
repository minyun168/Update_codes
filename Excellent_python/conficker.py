#define findtargets function
#using nmap-python to scan all of the hosts open the tcp/445 port

import nmap
def findtargets(subnet)
	nmapscan=nmap.PortScanner()
	nmapscan.scan(subnet,'445')
	
	targethosts=[]
	for host in nmapscan.all_hosts():
		if nmapscan[host].has_tcp(445):
			state=nmapscan[host]['tcp'][445]['state']
			if state == 'open':
				print('[+] Found Target Host:'+host)
				targethosts.append(host)
	return targethosts

