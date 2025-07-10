import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 3000))

while True:
    msg = input("Send:")
    client_socket.send(msg.encode())
    resp = client_socket.recv(1024).decode()
    print("Server response:", resp)


