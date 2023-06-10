import socket

client_socket = socket.socket()

port = 1234
server_address= '192.168.1.68'

client_socket.connect((server_address, port))

while True:

    print(client_socket.recv(1024).decode())
    client_socket.close()
    break
