import socket
import time

# Caesar Cipher utility functions
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# TCP Server
def tcp_server():
    host = '127.0.0.1'
    port = 12345
    shift = 3

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"TCP Server listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        encrypted_data = conn.recv(1024).decode()
        decrypted_data = decrypt(encrypted_data, shift)
        print(f"Received (encrypted): {encrypted_data}")
        print(f"Received (decrypted): {decrypted_data}")

        response = f"Server received: {decrypted_data}"
        encrypted_response = encrypt(response, shift)
        conn.send(encrypted_response.encode())

        conn.close()

# TCP Client
def tcp_client():
    host = '127.0.0.1'
    port = 12345
    shift = 3

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = "Hello, encrypted TCP server!"
    encrypted_message = encrypt(message, shift)
    print(f"Sending (original): {message}")
    print(f"Sending (encrypted): {encrypted_message}")
    client_socket.send(encrypted_message.encode())

    encrypted_response = client_socket.recv(1024).decode()
    decrypted_response = decrypt(encrypted_response, shift)
    print(f"Received from server (encrypted): {encrypted_response}")
    print(f"Received from server (decrypted): {decrypted_response}")

    client_socket.close()

# UDP Server
def udp_server():
    host = '127.0.0.1'
    port = 12346
    shift = 3

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"UDP Server listening on {host}:{port}")

    while True:
        encrypted_data, addr = server_socket.recvfrom(4096)
        encrypted_data = encrypted_data.decode()
        decrypted_data = decrypt(encrypted_data, shift)
        print(f"Received from {addr}")
        print(f"Encrypted: {encrypted_data}")
        print(f"Decrypted: {decrypted_data}")

        response = f"Server received: {decrypted_data}"
        encrypted_response = encrypt(response, shift)
        server_socket.sendto(encrypted_response.encode(), addr)

# UDP Client
def udp_client():
    server_address = ('127.0.0.1', 12346)
    shift = 3

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        message = "Hello, encrypted UDP Server!"
        encrypted_message = encrypt(message, shift)
        print(f"Sending (original): {message}")
        print(f"Sending (encrypted): {encrypted_message}")
        client_socket.sendto(encrypted_message.encode(), server_address)

        print("Waiting for response...")
        encrypted_data, server = client_socket.recvfrom(4096)
        encrypted_data = encrypted_data.decode()
        decrypted_data = decrypt(encrypted_data, shift)
        print(f"Received from {server}")
        print(f"Encrypted: {encrypted_data}")
        print(f"Decrypted: {decrypted_data}")

    finally:
        print("Closing socket")
        client_socket.close()

# Main function to run the desired component
def main():
    print("Choose a component to run:")
    print("1. TCP Server")
    print("2. TCP Client")
    print("3. UDP Server")
    print("4. UDP Client")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        tcp_server()
    elif choice == '2':
        tcp_client()
    elif choice == '3':
        udp_server()
    elif choice == '4':
        udp_client()
    else:
        print("Invalid choice. Please run the script again and select a number between 1 and 4.")

if __name__ == "__main__":
    main()
