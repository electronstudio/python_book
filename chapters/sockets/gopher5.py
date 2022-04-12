import socket

server = ("gopher.floodgap.com", 70)
page = ""
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server)
    sockFile = sock.makefile()
    sock.send(page.encode())
    sock.send(b"\r\n")
    links = []
    for line in sockFile.readlines():
        t = line[0]
        fields = line[1:].split('\t')
        if t == "i":
            print(fields[0])
        elif t == "1" or t == "0":
            print(len(links), fields[0])
            links.append(fields)
        else:
            print(t, fields[0])
    sockFile.close()
    n = int(input(">"))
    page = links[n][1]
    print(page)
