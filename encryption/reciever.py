from Crypto.Cipher import AES
import socket

key = b"0123456789123456"
nonce = b"0123456789123456"
con = AES.new(key, AES.MODE_EAX,nonce)


s = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
s.bind(("localhost",9999))
s.listen(1)

conn,address = s.accept()
new_file = open("new_file.txt","wb")

file_bytes = b""

while True:
    data = conn.recv(1024)
    if file_bytes[-5 : ] == b"<END>":
        break;
    else:
        file_bytes+=data

new_file.write(con.decrypt(file_bytes[:-5]))

new_file.close()
s.close()
