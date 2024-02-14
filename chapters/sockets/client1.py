import socket

server = "127.0.0.1"
port = 65439
sock = socket.create_connection((server, port))
sock.send(b"hello")
sock.close()

