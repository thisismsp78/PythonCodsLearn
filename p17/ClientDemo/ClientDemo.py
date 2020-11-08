import socket

print("Client")

host="127.0.0.1"
port=65331

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as _socket:
    _socket.connect((host,port))
    _socket.sendall(b"Test")
    data=_socket.recv(1024)
    print(repr(data))