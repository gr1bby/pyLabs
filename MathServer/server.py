from flask import Flask, render_template, request
from flask_migrate import Migrate

from calculation import calculate
from models import UserDatabaseInterphase
from config import postgresql as settings
# from MathServer.calculation import calculate
# from MathServer.models import UserDatabaseInterphase
# from MathServer.config import postgresql as settings


app = Flask(__name__)
db = UserDatabaseInterphase(
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
        return 'nice'
    else:
        return data


@app.route('/database', methods=['POST', 'GET'])
def get_database():
    return render_template('limit_and_offset.html')


@app.route('/database/answer', methods=['POST', 'GET'])
def get_database_by_operator():
    operator = request.form['operator']
    limit = int(request.form['limit'])
    offset = int(request.form['offset'])
    db.get_data(op=operator, limit=limit, offset=offset)
    return 'Success'


if __name__ == '__main__':
    
    db.create_database('data')
    app.run()
