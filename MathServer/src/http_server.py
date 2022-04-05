import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from flask import Flask, render_template, request
from flask_migrate import Migrate

import config as settings

from models import UserDatabaseInterfase
from calculation import calculate

from config import SERVER_HOST, SERVER_PORT


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


@app.route('/answer', methods=['POST', 'GET'])
def get_answer():
    data = calculate(request.form['data'])
    if isinstance(data, dict):
        db.insert_data(data)
        return str(data['result'])
    else:
        return data


@app.route('/database', methods=['POST', 'GET'])
def get_database():
    return render_template('limit_and_offset.html')


@app.route('/database/answer', methods=['POST', 'GET'])
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
    app.run(host=SERVER_HOST, port=SERVER_PORT)


if __name__ == '__main__':
    run_server()