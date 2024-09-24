# Sender (client.py)
import socket
import random

def encrypt_message(message):
    encrypted_message = ""
    keys = []
    for char in message:
        key = random.randint(1, 50)
        keys.append(key)
        encrypted_message += chr(ord(char) + key)
    return encrypted_message, keys

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('localhost', 6017))

    # Input the message from the user
    message = input("Enter the message to send: ")

    # Encrypt the message
    encrypted_message, keys = encrypt_message(message)
    key_string = ','.join(map(str, keys))

    # Send the encrypted message and keys to the server
    client_socket.send(f"{encrypted_message}|{key_string}".encode())

    print(f"Sent Encrypted Message: {encrypted_message}")
    print(f"Sent Keys: {keys}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
