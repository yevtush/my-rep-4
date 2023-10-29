import socket

# Створення клієнтського сокету
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345

client_socket.connect((host, port))
print(f"Під'єднано до сервера {host}:{port}")

while True:
    message = input("Повідомлення клієнта: ")
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print(f"Сервер: {data}")

client_socket.close()