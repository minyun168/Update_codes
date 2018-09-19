import ftplib
def anonLogin(hostname):
	try:
		ftp=ftplib.FTP(hostname)
		ftp.login('anonymous','me@your.com')
		print('\n[*] ' +str(hostname) +'ftp anonymous login succeeded')
		ftp.quit()
		return True
	except Exception as e:
		print ('\n[-] '+str(hostname)+ 'ftp anonymous login failed.')
		return False
host = '192.168.1.123'
anonLogin(host)

