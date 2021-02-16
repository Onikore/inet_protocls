import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9090))

# s.send((sys.argv[1] + "\r\n").encode())

# declares a bytes
response = b""
while True:
    data = s.recv(4096)
    response += data
    if not data:
        break
s.close()

# convert bytes to string
print(response.decode())
