import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get('PGUSER')
DB_PASS = os.environ.get('PGPASS')
DB_HOST = os.environ.get('PGHOST')
DB_PORT = int(os.environ.get('PGPORT'))
DB_NAME = os.environ.get('PGDB')


SERVER_HOST = '127.0.0.1'
SERVER_LOCAL_HOST = '0.0.0.0'
SERVER_PORT = 5000
