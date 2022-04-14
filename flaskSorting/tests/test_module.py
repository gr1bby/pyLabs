import unittest

from api import app
from config import Config
from logic.sorting import *
from logic.hashing import hash_list
from database.db_interfase import DatabaseInterfase
from database.model import DataModel


class TestLogic(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()


    def test_response_status_code(self):
        body = {
            'seq1': [1, 2, 3],
            'seq2': ['3', '4', '5']
        }

        response = self.app.post('/sort/insertion', data=body)
        self.assertEqual(response.status_code, 200)


    def test_sorting(self):
        sorted_insertion = [2, 3, 1]
        sorted_merge = [4, 1, -3]
        sorted_selection = ['b', 'a', 'h', 'd']
        sorted_quick = [7, 0, 6, -3, 9]

        insertion_sort(sorted_insertion)
        merge_sort(sorted_merge)
        selection_sort(sorted_selection)
        quick_sort(sorted_quick, 0, len(sorted_quick))

        self.assertEqual(sorted_insertion, [1, 2, 3])
        self.assertEqual(sorted_merge, [-3, 1, 4])
        self.assertEqual(sorted_selection, ['a', 'b', 'd', 'h'])
        self.assertEqual(sorted_quick, [-3, 0, 6, 7, 9])


    def test_hashing(self):
        seq1 = [1, 2, 3, 5, 4, 7, 6]
        seq2 = ['1', '2', '3', '5', '4', '7', '6']

        self.assertEqual(hash_list(seq1), '2c904439ce7608bd')
        self.assertEqual(hash_list(seq2), 'be35367c8d81151f')



class TestDatabase(unittest.TestCase):

    def setUp(self):
        config = Config()
        user = config.DB_USER
        password = config.DB_PASS
        host = config.DB_HOST
        port = config.DB_PORT
        db_name = 'test_db'

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


    def test_append_data(self):
        data = {
            'unsorted': 'b186d584fbd442b4',
            'sorted': '{0,1,2,5,43,124,147}',
        }

        self.db.insert_data(data)

        row_request = self.session.query(DataModel)
        response = self.connection.execute(str(row_request))
        self.assertTrue(len(response.fetchall()))
        self.connection.close()


if __name__ == '__main__':
    unittest.main()
