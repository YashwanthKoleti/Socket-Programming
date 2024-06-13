from Crypto.Cipher import AES
import socket

key = b"0123456789123456"
nonce = b"0123456789123456"
conn = AES.new(key, AES.MODE_EAX,nonce)


s = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
s.connect(("localhost",9999))

file = open("mayyaa","rb")
text = file.read()
encry_the_mess = conn.encrypt(text)

s.sendall(encry_the_mess)
s.send(b"<END>")
