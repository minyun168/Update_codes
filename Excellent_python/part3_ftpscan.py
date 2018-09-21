#search web page in the ftp server
#did not test
import ftplib

def returnDefault(ftp):
	


	weblist=ftp.nlst()	#ftp:ftp connect instance object
	retlist=[]
	for filename in weblist:
		fn=filename.lower()
		if ".index" in fn or '.php'in fn or '.htm' in fn or '.php' in fn:
			print("found web page"+filename)
			
			retlist.append(str(filename))
		else
			print("error")
	return retlist
host='192.168.1.123'
ftp=ftplib.FTP(host)
ftp.login('guest','password')
returnDefault(ftp)

