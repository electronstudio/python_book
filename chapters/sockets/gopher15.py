import socket
import time
from collections import namedtuple
from nicegui import ui

Page = namedtuple('Page', ['server', 'port', 'path', 'page_type'])
page = Page("gopher.floodgap.com", 70, "", "1")

links = {}
history = []


@ui.refreshable
def load_page():
    global links
    links = {}

    sock = socket.create_connection((page.server, page.port))
    sock.send(page.path.encode())
    sock.send(b"\r\n")

    if page.page_type == "0":
        load_page_0(sock)
    elif page.page_type == "1":
        load_page_1(sock)

    sock.close()
    server_input.value = page.server
    path_input.value = page.path


def load_page_0(sock):
    for line in sock.makefile(errors="replace").readlines():
        ui.html("<pre>" + line + "</pre>").style("margin-top: -1rem;")


def load_page_1(sock):
    for line in sock.makefile(errors="replace").readlines():
        line_type = line[0]
        fields = line[1:].split('\t')
        if line_type == "i":
            ui.html("<pre>" + fields[0] + "</pre>").style("margin-top: -1rem;")
        elif line_type == "1" or line_type == "0":
            b = ui.button(fields[0], on_click=click_button)
            links[b] = Page(fields[2], int(fields[3]), fields[1], line_type)
        elif line_type == "h":
            ui.link(fields[0], fields[1][4:], new_tab=True)
        else:
            ui.html("<pre>" + line + "</pre>").style("margin-top: -1rem;")


def click_button(b):
    global page
    history.append(page)
    page = links[b.sender]
    load_page.refresh()


def back_button():
    global page
    page = history.pop()
    load_page.refresh()


def go_button():
    global page
    page = Page(server_input.value, 70, path_input.value, "1")
    history.append(page)
    load_page.refresh()


with ui.header():
    ui.button("back", on_click=back_button)
    server_input = ui.input('server')
    path_input = ui.input('path')
    ui.button("go", on_click=go_button)

load_page()

ui.run()
