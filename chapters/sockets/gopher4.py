import socket
server = ("gopher.floodgap.com", 70)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server)
sockFile = sock.makefile()
sock.send(b"\r\n")
for line in sockFile.readlines():
    t = line[0]
    text = line[1:].split('\t')
    if t == "i":
        print(text[0])
    else:
        print(text)
sockFile.close()

