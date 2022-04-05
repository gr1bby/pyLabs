import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import socket
import json

import config as settings

from models import UserDatabaseInterfase
from calculation import calculate

from config import SERVER_HOST, SERVER_PORT


db = UserDatabaseInterfase(
    settings.DB_USER,
    settings.DB_PASS,
    settings.DB_HOST,
    settings.DB_PORT,
    settings.DB_NAME
)


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((SERVER_HOST, SERVER_PORT))
    server.listen(0)
    print("Waiting connection...")
    with server:
        while True:
            connection, client_address = server.accept()
            try:
                print(f"Connected to {client_address}")
                data = connection.recv(64)
                decoded_data = data.decode()
                if 'stop' in decoded_data or 'quit' in decoded_data:
                    break
                if 'getdata' in decoded_data:
                    operator = ''
                    limit = offset = 0
                    
                    splited_data = decoded_data.split()[1:]

                    match len(splited_data):
                        case 1:
                            operator = splited_data[0]
                        case 2:
                            operator, limit = splited_data
                        case 3:
                            operator, limit, offset = splited_data

                    try:
                        limit = int(limit)
                    except ValueError:
                        limit = 0
                    try:
                        offset = int(offset)
                    except ValueError:
                        offset = 0
                    
                    result_json = db.get_data(op=operator, limit=limit, offset=offset)
                    result = json.dumps(result_json)
                    connection.sendall(result.encode())

                else:
                    result = calculate(decoded_data)
                    db.insert_data(result)
                    connection.sendall(result['result'].encode())

                print(f"Sended: {result}")
            finally:
                print("Connection closed.")
                connection.close()           
