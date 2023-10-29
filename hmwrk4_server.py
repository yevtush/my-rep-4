import socket

# Створення серверного сокету
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Сервер слухає на {host}:{port}")

# Прийом та обробка з'єднання
client_socket, addr = server_socket.accept()
print(f"З'єднання встановлене з {addr}")

while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(f"Клієнт: {data}")
    response = input("Відповідь сервера: ")
    client_socket.send(response.encode())

client_socket.close()