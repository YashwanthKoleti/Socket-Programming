from Crypto.Cipher import AES

message = b"hello world"

key = b"0123456789123456"
non = b"0123456789123456"

conn = AES.new(key,AES.MODE_EAX,non)
encr = conn.encrypt(message)
print(encr)
conn = AES.new(key,AES.MODE_EAX,non)
encr = conn.decrypt(encr)
print(encr)