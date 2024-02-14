import socket

sock = socket.create_server(("0.0.0.0", 65439))
while True:
    sock.listen()
    connection, address = sock.accept()
    message = connection.makefile().readline()
    print("received: ", message, "from:", address)
