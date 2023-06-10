import socket

my_socket = socket.socket()
print("Socket has been created....")

port = 1234
my_socket.bind(('',port))
print("Socket is binded to a port")

my_socket.listen(3) # putting socket into listening mode
print("Server socket is listening now...")

while True:
    client, address = my_socket.accept()
    print("Got connection from client ",client, " and address = ", address)
    client.send("Connection request is received by me.".encode())

    break
    

