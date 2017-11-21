import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 80
host = 'data.pr4e.org'
mysock.connect((host, port))
message = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'

mysock.send(message.encode())

while True:
    data = mysock.recv(512).decode()
    if len(data)< 1:
        break
    print(data)

mysock.close()