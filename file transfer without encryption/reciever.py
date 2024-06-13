import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",6000))

file = open("recieved file.png","wb")
file_bytes = b""

while True:
    data = s.recv(1024)
    if file_bytes[-7 : ] == b"<Ayipe>":
        break;

    else:
        file_bytes += data


file.write(file_bytes)
file.close()
s.close()
