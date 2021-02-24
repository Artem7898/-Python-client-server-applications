import socket

# Задаем адрес сервера
SERVER_ADDRESS = ('localhost', 8888)

# Настраиваем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(10)
print('сервер работает, пожалуйста, нажмите ctrl + c для остановки')

# Слушаем запросы
while True:
    connection, address = server_socket.accept()
    print("new connection from {address}".format(address=address))

    data = connection.recv(1024)
    print(str(data))

    connection.send(bytes('Привет я сервер!', encoding='UTF-8'))

    connection.close()
