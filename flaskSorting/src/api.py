from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from flask import Flask, jsonify, request

from DBInterfase import DatabaseInterfase
from timer import Timer
from config import Config

import handler


app = Flask(__name__)

timer = Timer()
settings = Config()

db = DatabaseInterfase(
    settings.DB_USER,
    settings.DB_PASS,
    settings.DB_HOST,
    settings.DB_PORT,
    settings.DB_NAME
)

executor = ProcessPoolExecutor()


@app.route('/api/<string:sort_method>', methods=['POST'])
def sorting_api(sort_method: str):
    if request.headers.get('Content-type') == 'application/json':
        response_data = request.get_data()
        
        print(type(response_data))
        
        future = executor.submit(handler.get_sorted_answer, response_data, sort_method)
        data = future.result()
        # executor.shutdown()

        return jsonify(data)
    else:
        print(request)
        return 'not ok'
    

def run_server():
    db.create_tables()
    app.run()


if __name__ == '__main__':
    run_server()
