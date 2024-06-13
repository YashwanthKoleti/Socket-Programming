import os
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.0.1"
port = 6000

s.bind((host,port))
s.listen(5)

conn, address = s.accept()
print("connected")
f = open("hey.png","rb")
data = f.read()

conn.sendall(data)
conn.send(b"<Ayipe>")
conn.close()
s.close()