# from os import getenv
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get('PGUSER')
DB_PASS = os.environ.get('PGPASS')
DB_HOST = os.environ.get('PGHOST')
DB_PORT = int(os.environ.get('PGPORT'))
DB_NAME = os.environ.get('PGDB')


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000


# DB_USER = getenv('pguser', default='postgres')
# DB_PASS = getenv('pgpasswd', default='1234')
# DB_HOST = getenv('pghost', default='localhost')
# DB_PORT = getenv('pgport', default=5432)
# DB_NAME = getenv('pgdb', default='math_data')
