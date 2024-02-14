import socket
import time
from collections import namedtuple
from nicegui import ui

Page = namedtuple('Page', ['server', 'port', 'path'])
page = Page("gopher.floodgap.com", 70, "")

links = {}

@ui.refreshable
def load_page():
    global links
    links = {}

    sock = socket.create_connection((page.server, page.port))
    sock.send(page.path.encode())
    sock.send(b"\r\n")

    for line in sock.makefile(errors="replace").readlines():
        line_type = line[0]
        fields = line[1:].split('\t')
        if line_type == "i":
            ui.html("<pre>" + fields[0] + "</pre>").style("margin-top: -1rem;")
        elif line_type == "1" or line_type == "0":
            b = ui.button(fields[0], on_click=click_button)
            links[b] = Page(fields[2], int(fields[3]), fields[1])
        else:
            ui.html("<pre>" + line + "</pre>").style("margin-top: -1rem;")

    sock.close()

def click_button(b):
    global page
    page = links[b.sender]
    load_page.refresh()

load_page()

ui.run()
