import socket

s = socket.socket()

hostname = socket.gethostname()
print hostname
port=10000
s.connect((hostname,port))
print s.recv(1024)