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

