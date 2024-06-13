import socket
import rsa
import threading
from queue import Queue


#Threads
NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()

#creating a bool to chck whether connection is still there or disconneted
check = 1

# Global socket variable
sock = None

# Load public and private keys
with open('publicKey_of_Person1.pem', 'rb') as f:
    Public_key_of_reciever = rsa.PublicKey.load_pkcs1(f.read())

with open('privateKey_of_Person2.pem', 'rb') as f:
    Private_key = rsa.PrivateKey.load_pkcs1(f.read())


# Prompt user for action
print('Do you want to host(press 1) or connect(press 2): ')
cmd = input().strip()

if cmd == '1':
    print('Making a server...')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9997))
    s.listen(10)
    conn, address = s.accept()
    print("connected to " + address[0])
    conn.sendall(b'connected to server')
    sock = conn
    #using sock to avoid errors,
    # because if cmd = 2 then conn.send doesn't exist

elif cmd == '2':
    print('connecting to server....')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 9997))
    data = s.recv(1024)
    print(data.decode())
    sock = s

def encrypt_message(message):
    return rsa.encrypt(message.encode(), Public_key_of_reciever)

def decrypt_message(message):
    try:
        return rsa.decrypt(message, Private_key).decode()
    except rsa.DecryptionError:
        return "Failed to decrypt message"

def send_messages():
    global sock
    global check
    while check:
        cmd = input()
        if cmd == 'quit':
            sock.sendall(b'quit')
            check = 0
        if cmd and check:
            encrypted_message = encrypt_message(cmd)
            sock.sendall(encrypted_message)
            print(f"Sent: {cmd}")

def receive_messages():
    global sock
    global check
    while check:
        try:
            data = sock.recv(1024)
            if not data:
                break
            if data == b'quit':
                print('the sender has disconnected, please enter quit to close the program')
                check = 0
            if data and check:
                decrypted_message = decrypt_message(data)
                print(f"Received: {decrypted_message}")
        except ConnectionResetError:
            print("Connection was closed by the server.")
            check = 0
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        x = queue.get()
        if x == 1:
            send_messages()
        elif x == 2:
            receive_messages()
        queue.task_done()

def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()

# Start the threads and jobs
create_workers()
create_jobs()

if cmd == 1:
    conn.close()

s.close()