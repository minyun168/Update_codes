part2_of_portscan.py
import optparse
from socket import *
def connScan (tgtHost,tgtPort):
	try:
		