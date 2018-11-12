#Tcp_client

import socket

target_host = "www.baidu.com"
target_port = "80"

#build a socket object 
client = socket.socket(socket.AF_INET,socket.socket_STREAM)

#connect client
client.connect((target_host,target_port))

#send some data
client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

#receive some data
response = client.recv(2048)

print response
