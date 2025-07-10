import socket

server_socket = socket.socket()
server_socket.bind(('localhost', 3000))
server_socket.listen(1)

print("server is listening on port 3000...")

conn, addr = server_socket.accept()
print(f"Connected on {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("Client: ", data)
    send = input("To send: ")
    conn.send(f"{send}".encode())

conn.close()
