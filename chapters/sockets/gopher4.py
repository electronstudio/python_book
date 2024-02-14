import socket

server = "gopher.floodgap.com"
port = 70
sock = socket.create_connection((server, port))
sock.send(b"\r\n")

for line in sock.makefile().readlines():
    line_type = line[0]
    fields = line[1:].split('\t')
    if line_type == "i":
        print(fields[0])
    else:
        print(line)

sock.close()

