import socket

host = "127.0.0.1"
port = 5678

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

try:
    print("Connected to " + host + "."+str(port))
except:
    print("connection failed")

while True:
    cmd = input()
    cmd = str(cmd)

    if len(cmd) > 0:
        if cmd == 'quit':
            s.close()
            print("connection closed")
            break;
        else:
            s.send(cmd.encode('utf-8'))

    data = s.recv(1024).decode('utf-8')
    if len(data) > 0:
        print("Person 1:" + data)
