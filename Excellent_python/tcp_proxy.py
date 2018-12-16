#

import sys
import socket
imoort threading

sef server_loop(local_host,local_port,remote_host,remote_port,receive_first):
	
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	try:
		server.bind((local_host,local_port))
	except:
		print "[!!]Failed to listem on %s:%d" %(local_host, local_port)
		print "[!!] check for other listening sockets or correct permission."
		sys.exit(0)

	print "[*] Listening on %s:%d" %(local_host,local_port)

	srver.listem(5)

	while True:

		client_socket, addr = server.accept()
		print "[==>+] Received incoming connection from %s:%dd" %(addr[0],addr[1])
		proxy_thread = threading.Threading(target=proxy_handler,arg=(lient_socket,remote_port,receive_first))

		proxy_thread.start()