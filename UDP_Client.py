# -*- coding: utf-8 -*-
import socket
import caesar_cipher



def UDP_client(IP, PORT):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # Get the message from the user
        message = input("Enter a message: ")

        # Send the message to the server
        client_socket.sendto(message.encode(), (IP, PORT))

        # Receive the response from the server
        data, address = client_socket.recvfrom(1024)

        # Decode the received data
        response = data.decode()

        print(f"Received response from {address}: {caesar_cipher.decrypt_caesar(response, 3)}")


if __name__ == '__main__':
    # Set the IP address and port number
    IP = "127.0.0.1"
    PORT = 65432
    UDP_client(IP, PORT)