# Tcp server

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

#client process thread
def handle_client(client_socket):
	
	#print content of client sent
	request = client_socket.recv(1024)
	print "[*] Received: %s" %request

	#return a data package
	client_socket.send("ack")
	client_socket.close()

while True:
	
	client,addr = server.accept()

	print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])

	#hand up client thread, process input data
	client_handler = threading.Thread(target = handle_client,args = (client,))
	client_handler.start()