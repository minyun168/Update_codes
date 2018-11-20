#netcat 

import sys 
import socket
import getopt
import threading
import subprocess

#define global variable
listen = False 
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

#
def usage():
	print "bhp net tool"
	print 
	print "usage: bhpnet.py -t target_port -p port"
	print "-l --list  "
	...



def main():
	global listen
	global port 
	global execute
	global command
	global upload_destination
	global target 

	if not len(sys.argv[1:]):
		usage()

	#read the options of input command 
	try:
		opts,args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","execute","target","port","command","upload"])
	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o,a in opts:
		if o in ("-h","--help"):
			usage()
		elif o in ("-l","--listen"):
			listen = True
		elif o in ()




main()


def client_sender(buffer):
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	try:
		#connect to target host
		client.connect((target,port))

		if len(buffer):          #1:
			client.send(buffer)


		while true:
			#
			#now wait for data of responsing 
			recv_len = 1
			response = ""

			while recv_len:      #2:
				data = client.recv(4096)
				recv_len = len(data)
				response+= data

				if recv_len < 4096:
					break
				
			print response

			#wait for more input
			buffer = raw_input("")   #3:
			buffer += "\n"

			#send buffer
			client.send(buffer)

	except:
		print "[*] Exception! Exiting."
    	client.close()



def server_loop():
	global target

	#
	if not len(target):
		target = "0.0.0.0"

	server = socket.socket(socket.AF_INET,socket.SOCK_SREAM)
	server.bind((target,port))

	server.listen(5)

	while True:
		client_socket,addr = server.accept()

		#
		client_thread = threading.Thread(target = client_handler, args = (client_socket,))
		client_thread.start()

def run_command(command):

	#
	command = command.rstrip()

	#
	try:
		output = subprocess.check_out(command,stderr=subprocess.STDOUT,shell=True)
	except:
		output = "Failend to execute command.\r\n"

	#
	return output






