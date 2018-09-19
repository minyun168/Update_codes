#This is a part1 of portscan
import optparse
parser=optparse.OptionParser('usage %prog -H'+\
	'<target host> -p <target port>')
parser.add_option('-H',dest='tgtHost',type='string',\
	help='specify target host')
parser.add_option('-p',dest='tgtHost',type='int',\
	help='specifiy target port')
(options,args)=parser.parse_args()
tgtHost=options.tgtHost
tgtHost=options.tgtPort
if (tgtHost == None) | (tgtPort == None):
	print parser.usage
	exit()
