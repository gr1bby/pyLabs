import unittest

from api import app
from config import Config
from logic.sorting import *
from logic.hashing import hash_list
from logic.handler import get_sorted_answer
from logic.json_handler import JSONDecoder, JSONEncoder
from database.db_interfase import DatabaseInterfase
from database.model import DataModel


DATA = {
    'seq1': [1, 5, 6, 4, 3],
    'seq2': [3, 6, -9, 5, 7],
    'seq3': [4, 7, -5, 1, 9],
    'seq4': [2, 8, -3, 0, 4]
}


class TestAPI(unittest.TestCase):

    def setUp(self):
        app.testing = True
        app.json_decoder = JSONDecoder
        app.json_encoder = JSONEncoder
        self.app = app.test_client()

        config = Config()
        user = config.DB_USER
        password = config.DB_PASS
        host = config.DB_HOST
        port = config.DB_PORT
        db_name = config.DB_NAME

        self.db = DatabaseInterfase(
            user,
            password,
            host,
            port,
            db_name
        )

        self.db.create_tables()
        self.engine = self.db._DatabaseInterfase__engine
        self.session = self.db._DatabaseInterfase__session
        self.connection = self.engine.connect()


    def tearDown(self):
        self.db.drop_table()


    def test_method_insertion(self):
        response = self.app.post('/sort/insertion', json=DATA)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json)
        self.assertEqual(len(response.json.keys()), 4)

        row_request = self.session.query(DataModel)
        response = self.connection.execute(str(row_request))
        self.assertEqual(len(response.fetchall()), 4)
        self.connection.close()

    
    def test_method_merge(self):
        response = self.app.post('/sort/merge', json=DATA)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json)
        self.assertEqual(len(response.json.keys()), 4)

        row_request = self.session.query(DataModel)
        response = self.connection.execute(str(row_request))
        self.assertEqual(len(response.fetchall()), 4)
        self.connection.close()


    def test_method_selection(self):
        response = self.app.post('/sort/selection', json=DATA)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json)
        self.assertEqual(len(response.json.keys()), 4)

        row_request = self.session.query(DataModel)
        response = self.connection.execute(str(row_request))
        self.assertEqual(len(response.fetchall()), 4)
        self.connection.close()


    def test_method_quick(self):
        response = self.app.post('/sort/quick', json=DATA)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json)
        self.assertEqual(len(response.json.keys()), 4)

        row_request = self.session.query(DataModel)
        response = self.connection.execute(str(row_request))
        self.assertEqual(len(response.fetchall()), 4)
        self.connection.close()
            

if __name__ == '__main__':
    unittest.main()
