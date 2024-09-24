# Receiver (server.py)
import socket

def decrypt_message(encrypted_message, keys):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        decrypted_message += chr(ord(encrypted_message[i]) - keys[i])
    return decrypted_message

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind(('localhost', 6017))

    # Start listening for incoming connections
    server_socket.listen(1)
    print("Server is listening...")

    # Accept the connection from the client
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive the data from the client
    data = conn.recv(1024).decode()

    # Split the received data into encrypted message and keys
    encrypted_message, key_string = data.split('|')
    keys = list(map(int, key_string.split(',')))

    print(f"Received Encrypted Message: {encrypted_message}")
    print(f"Received Keys: {keys}")

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, keys)
    print(f"Decrypted Message: {decrypted_message}")

    # Close the connection
    conn.close()

if __name__ == "__main__":
    start_server()
