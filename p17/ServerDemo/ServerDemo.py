import socket

print("Server")

host="127.0.0.1"
port=65331

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as _socket:
    _socket.bind((host,port))
    _socket.listen()
    connection,address=_socket.accept()
    print("Connection from ",address)
    with connection:
        while True:
            data=connection.recv(1024)
            if not data:
                break
            print(data.decode("ascii"))
            connection.sendall(data)