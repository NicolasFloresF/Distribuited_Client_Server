from socket import *

s = socket(AF_INET, SOCK_STREAM)
HOST = "localhost"
PORT = 5050
s.connect((HOST, PORT))
s.send("hello, world".encode())

data = s.recv(1024)
print(data.decode())
s.close()
