import socket

server = "gopher.floodgap.com"
port = 70
sock = socket.create_connection((server, port))
sock.send(b"\r\n")

for line in sock.makefile().readlines():
    print(line[1:].split('\t'))

sock.close()

