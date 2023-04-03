# -*- coding: utf-8 -*-
import socket
import caesar_cipher

def server_udp(IP, PORT):

    # Create a socket object
    # socket.SOCK_DGRAM це UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the IP address and port number
    server_socket.bind((IP, PORT))

    print("UDP Server is listening...")

    while True:
        # Receive the data and address from the client
        data, address = server_socket.recvfrom(1024)

        # Decode the received data
        message = data.decode()

        print(f"Received message from {address}: {message}")

        # Send a response back to the client
        response = f"hello, {message}".lower()
        response = caesar_cipher.decrypt_caesar(response, 3)
        server_socket.sendto(response.encode(), address)


if __name__ == '__main__':
    # Set the IP address and port number
    IP = "127.0.0.1"
    PORT = 65432
    server_udp(IP, PORT)