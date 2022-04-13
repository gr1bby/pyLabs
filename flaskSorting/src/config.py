import os
from dotenv import load_dotenv


class Config:

    def __init__(self):
        load_dotenv()

        self.DB_USER = os.environ.get('PGUSER')
        self.DB_PASS = os.environ.get('PGPASS')
        self.DB_HOST = os.environ.get('PGHOST')
        self.DB_PORT = int(os.environ.get('PGPORT'))
        self.DB_NAME = os.environ.get('PGDB')
