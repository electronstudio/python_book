import socket

server = "gopher.floodgap.com"
port = 70
path = "/ffsl/ffsl.txt"
sock = socket.create_connection((server, port))
sock.send(path.encode())
sock.send(b"\r\n")

for line in sock.makefile().readlines():
    line_type = line[0]
    fields = line[1:].split('\t')
    if line_type == "i":
        print(fields[0])
    else:
        print(line)

sock.close()

"""
    for line in sock.makefile().readlines():
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen codecs>", line 322, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa9 in position 1086: invalid start byte


https://docs.python.org/3/library/functions.html#open
"""