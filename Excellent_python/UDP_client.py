#UDP_client

import socket

target_host = "127.0.0.1"
target_port = 80

#
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#UDP have not connect state
#
client.sendto("hhhhhhh",(target_host,target_port))

#
data,addr = client.recvfrom(2048)

print data
