import socket
from collections import namedtuple

Page = namedtuple('Page', ['server', 'port', 'path'])
page = Page("gopher.floodgap.com", 70, "")

links = []


def load_page():
    global links
    links = []

    sock = socket.create_connection((page.server, page.port))
    sock.send(page.path.encode())
    sock.send(b"\r\n")

    for line in sock.makefile(errors="replace").readlines():
        line_type = line[0]
        fields = line[1:].split('\t')
        if line_type == "i":
            print(fields[0])
        elif line_type == "1" or line_type == "0":
            print(len(links), fields[0])
            links.append(Page(fields[2], int(fields[3]), fields[1]))
        else:
            print(line)

    sock.close()


while True:
    print(page)
    load_page()
    n = int(input(">"))
    page = links[n]
