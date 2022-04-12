import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 65439))
while True:
    sock.listen()
    connection, address = sock.accept()
    message = connection.makefile().readline()
    print("received: ", message, "from:", address)
