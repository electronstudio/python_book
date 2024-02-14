import socket

server = "gopher.floodgap.com"
port = 70
path = ""
sock = socket.create_connection((server, port))
sock.send(path.encode())
sock.send(b"\r\n")

links = []
for line in sock.makefile(errors="replace").readlines():
    line_type = line[0]
    fields = line[1:].split('\t')
    if line_type == "i":
        print(fields[0])
    elif line_type == "1" or line_type == "0":
        print(len(links), fields[0])
        links.append(fields)
    else:
        print(line)

sock.close()
