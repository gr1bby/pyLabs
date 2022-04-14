from concurrent.futures import ProcessPoolExecutor

from flask import Flask, jsonify, request

import config
import logic.handler as handler

from database.db_interfase import DatabaseInterfase
from logic.timer import Timer
from logic.json_handler import JSONEncoder, JSONDecoder


app = Flask(__name__)

timer = Timer()
settings = config.Config()

db = DatabaseInterfase(
    settings.DB_USER,
    settings.DB_PASS,
    settings.DB_HOST,
    settings.DB_PORT,
    settings.DB_NAME
)

executor = ProcessPoolExecutor()


@app.route('/sort/<string:sort_method>', methods=['POST'])
def sorting_api(sort_method: str):
    if request.headers.get('Content-type') == 'application/json':
        response_data = request.get_json() 
        future = executor.submit(handler.get_sorted_answer, response_data, sort_method)
        data = future.result()
        return jsonify(data)
    else:
        return 'Bad response'
    

def run_server():
    app.json_decoder = JSONDecoder
    app.json_encoder = JSONEncoder
    db.create_tables()
    app.run(host=settings.SERVER_LOCAL_HOST, port=5050)


if __name__ == '__main__':
    run_server()
