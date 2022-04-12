import socket
server = ("gopher.floodgap.com", 70)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server)
sock.send(b"\r\n")
for line in sock.makefile().readlines():
    print(line)
sock.close()

