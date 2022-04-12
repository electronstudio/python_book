import socket

server = ("127.0.0.1", 65439)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server)
sock.send(b"hello")
sock.close()

