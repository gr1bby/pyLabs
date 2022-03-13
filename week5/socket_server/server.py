import socket
import operator
from typing import Any


HOST, PORT = '127.0.0.1', 4447


def send_error(exception: Any) -> str:
    print(f"{type(exception).__name__}: {exception}")
    return ''


def calculate(data: str) -> str:
    splited_data = data.split()
    try:
        func_name = splited_data[0]
        num1 = float(splited_data[1])
        num2 = float(splited_data[2])
        return str(operator.methodcaller(func_name, num1, num2)(operator))
    except ValueError as ex:
        return send_error(ex)
    except AttributeError as ex:
        return send_error(ex)
    except ZeroDivisionError as ex:
        return send_error(ex)
    except IndexError as ex:
        return send_error(ex)


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(0)
    print("Waiting connection...")
    with server:
        while True:
            connection, client_address = server.accept()
            try:
                print(f"Connected to {client_address}")
                data = connection.recv(16)
                decoded_data = data.decode()
                if 'stop' in decoded_data or 'quit' in decoded_data:
                    break
                result = calculate(decoded_data)
                connection.sendall(result.encode())
                print(f"Sended: {result}")
            finally:
                print("Connection closed.")
                connection.close()           
