#Exercises1_of_pexpect

import pexpect
PROMPT = ['# ','>>> ','> ','\s ']

def send_command (child,cmd):
	child.expect(PROMPT)
	child.sendline(cmd)
	print child.before

def connect(user, host, password):
	ssh_newkey = 'ssh ' + user + '@' +host
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT,ssh_newkey),'[P|p]assword:'])
	if ret === 0:
		print '[-] Errot connecting'
		return
	if ret ==1:
	child.sendline('yes')
	ret =child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
	if ret == 0:
		print '[-] Error Connecting'
		return
	child.sendline(password)
	child.expect(PROMPT)
	return child
	
