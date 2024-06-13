import socket
from Crypto.Cipher import AES
import threading
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9997))
s.listen(10)
conn, address = s.accept()
print("connected to "+ address[0])

key = b"0123456789123456"
nonce = b"0123456789123456"

def encrypt_message(message):
    encry = AES.new(key,AES.MODE_EAX,nonce)
    encry_mess = encry.encrypt(message.encode())
    return encry_mess

def decrypt_message(message):
    decry = encry = AES.new(key,AES.MODE_EAX,nonce)
    decry_mess = decry.decrypt(message)
    return decry_mess.decode()


def send_messages():
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            break
        if cmd:
            conn.sendall(encrypt_message(cmd))
            print(f"Server: {cmd}")



def receive_messages():
    while True:
        data = decrypt_message(conn.recv(1024))
        if data:
            print(f"Client: {data}")

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

create_workers()
create_jobs()
s.close()