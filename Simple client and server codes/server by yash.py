import socket

host = "localhost"
port = 5678
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))

s.listen((5))

conn,address = s.accept()
print("Connected to " + address[0] + "."+str(address[1]))

while True:

    message = conn.recv(1024).decode("utf-8")
    if len(message) > 0 :
        print("message from Person 1 : " + str(message))

    cmd = input()
    cmd = str(cmd)

    if len(cmd) > 0:
        if cmd == 'quit':
            conn.close()
            break;

        else :
            conn.sendall(cmd.encode('utf-8'))

s.close()