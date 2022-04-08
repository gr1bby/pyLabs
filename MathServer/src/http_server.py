from concurrent.futures import ProcessPoolExecutor

from flask import Flask, render_template, request
from flask_migrate import Migrate

import config as settings

from models import UserDatabaseInterfase
from calculation import calculate

from config import SERVER_LOCAL_HOST


app = Flask(__name__, template_folder='templates')
db = UserDatabaseInterfase(
    settings.DB_USER,
    settings.DB_PASS,
    settings.DB_HOST,
    settings.DB_PORT,
    settings.DB_NAME
)
migrate = Migrate(app, db)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/answer', methods=['POST'])
def get_answer():
    with ProcessPoolExecutor() as executor:
        future = executor.submit(calculate, request.form['data'])
        data = future.result()
        if isinstance(data, dict):
            db.insert_data(data)
            return str(data['result'])
        else:
            return data


@app.route('/database', methods=['GET'])
def get_database():
    return render_template('limit_and_offset.html')


@app.route('/database/answer', methods=['POST'])
def get_database_by_operator():
    limit = offset = 0
    operator = request.form['operator']
    try:
        limit = int(request.form['limit'])
    except ValueError:
        result = 'Bad values'
    try:
        offset = int(request.form['offset'])
    except ValueError:
        result = 'Bad values'

    result = db.get_data(op=operator, limit=limit, offset=offset)

    return render_template('database.html', result_list=result)


def run_server():
    db.create_database()
    app.run(host=SERVER_LOCAL_HOST)


if __name__ == '__main__':
    run_server()