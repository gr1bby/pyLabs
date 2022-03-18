from flask import Flask, render_template, request


from MathServer.calculation import calculate


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/answer', methods=['POST', 'GET'])
def get_answer():
    return calculate(request.form['data'])
