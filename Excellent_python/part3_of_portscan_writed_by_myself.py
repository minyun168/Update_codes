part3_of_portscan_writed_by_myself.py
import optparse
import socket
from socket import *
def connScan(tgtHost, tgtPort):
	try:
		connSkt= socket(AF_INET, SOCK_STREAM)
		connSkt.connect(())
