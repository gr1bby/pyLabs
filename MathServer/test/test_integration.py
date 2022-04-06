import unittest

import models, http_server
from calculation import calculate


DATA_FOR_APPEND = (
    {'data': 'add 5 2'},
    {'data': 'add -5.6 7'},
    {'data': 'add 5 11.22'},
    {'data': 'pow 5 7'},
    {'data': 'mul 5 7'},
    {'data': 'mul 4.32 -3.56'}
)


class TestIntegrationHttp(unittest.TestCase):
    def setUp(self):
        http_server.app.testing = True
        self.app = http_server.app.test_client()

        self.db = http_server.db
        self.db.create_database()

        self.engine = self.db._UserDatabaseInterfase__engine
        self.session = self.db._UserDatabaseInterfase__session
        self.connection = self.engine.connect()


    def tearDown(self):
        self.db.drop_table()


    def test_main_page_connection(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)


    def test_appending_data(self):
        for data in DATA_FOR_APPEND:
            response = self.app.post('/answer', data=data)  
            self.assertEqual(response.status_code, 200)

            answer = calculate(data['data'])
            result = float(response.get_data(as_text=True))
            self.assertEqual(result, answer['result'])

        row_request = self.session.query(models.DataModel)
        response = self.connection.execute(str(row_request))
        self.assertEqual(len(response.fetchall()), 6)
        self.connection.close()


    def test_database_page_connection(self):
        response = self.app.get('/database')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
