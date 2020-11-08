
import socket

print("Client")

host="127.0.0.1"
port=65331
username=input("Username : ")

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as _socket:
    _socket.connect((host,port))
    while True:
        message=input("Enter new message : ")
        _socket.sendall(f"{username} : {message}".encode())
        data=_socket.recv(1024)
        print(data.decode("ascii"))