# -*- coding: utf-8 -*-
import socket

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# sock = socket.socket() # за замовчуванням TCP
# sock.bind((HOST, PORT))
# sock.listen(1) # кількість клієнських яких обслуговує сервер
# conn, addr = sock.accept() # блокуєдодаток до тих пір поки не надійде повідомлення від клієнта
# # conn це зєднання
# # addr це адеса
#
# print('Connected by', addr)
#
# while True:
#     # recy читає дані із сокету приймає максимальну кількість байтів що може надійти в обному повідомленні
#     data = conn.recv(1024)
#     if not data:
#         break
#     # send відправляє дані із сокету у зворотньому напрямку
#     conn.send(data.upper())
#
# conn.close()


"""
Після отримання даних сервер закривається
"""


# socket.AF_INET - сокет буде обслуговуватись через апі адресу
# socket.SOCK_STREAM - тип нашого сокету, тобто TCP протокол для його створення

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data.upper())


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 65432)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data.upper())
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
