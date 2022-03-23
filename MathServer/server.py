from re import template
from flask import Flask, render_template, request
from flask_migrate import Migrate

from calculation import calculate
from models import UserDatabaseInterfase
from config import postgresql as settings
# from MathServer.calculation import calculate
# from MathServer.models import UserDatabaseInterphase
# from MathServer.config import postgresql as settings


app = Flask(__name__)
db = UserDatabaseInterfase(
    settings['pguser'],
    settings['pgpasswd'],
    settings['pghost'],
    settings['pgport'],
    settings['pgdb']
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
        return 'Success'
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


if __name__ == '__main__':
    db.create_database('data')
    app.run()
