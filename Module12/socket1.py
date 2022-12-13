import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketvar:
    socketvar.connect(("data.pr4e.org", 80))
    cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
    socketvar.send(cmd)

    while True:
        data = socketvar.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end="")
