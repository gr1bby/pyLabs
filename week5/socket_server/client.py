import socket
import sys


HOST, PORT = '127.0.0.1', 4447


if __name__ == '__main__':
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        message = ' '.join(sys.argv[1:])
        data = message.encode()
        client.sendall(data)
        received_data = client.recv(16).decode()
        try:
            result = float(received_data)
            print(f"Received data: {result:.4f}")
        except ValueError:
            print("Nothing is received")
    finally:
        print("Connection closed.")
        client.close()