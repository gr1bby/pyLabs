import requests

from multiprocessing import Pool, cpu_count
from typing import List

from flask import Flask, jsonify, request, render_template

from timer import Timer


app = Flask(__name__)
timer = Timer()


def get_urls(count: int) -> List[str]:
    urls = list()
    with open('urls', 'r') as file:
        for _ in range(count):
            urls.append(file.readline().rstrip('\n'))
    return urls


def send_request(url: str) -> int:
    try:
        response = requests.head(url)
        if response.status_code == 405:
            response = requests.get(url)
        # print(url + ' ' + str(response.status_code))

        return response.status_code
        
    except requests.exceptions.ConnectionError:
        return 400


def multi_send(urls: List[str]) -> dict:
    good_resp = bad_resp = 0

    with timer:
        with Pool(processes=cpu_count()) as processes:
            all_answers = processes.map(send_request, urls)
            for answer in all_answers:
                if 200 <= answer < 400:
                    good_resp += 1
                else:
                    bad_resp += 1
    
    return {
        'time': timer.time,
        'good': good_resp,
        'bad': bad_resp,
    }


def send_requests(urls: List[str]) -> dict:
    good_resp = bad_resp = 0
    with timer:
        for url in set(urls):
            response = send_request(url)
            if 200 <= response < 400:
                good_resp += 1
            else:
                bad_resp += 1

    return {
        'time': timer.time,
        'good': good_resp,
        'bad': bad_resp,
    }


@app.route('/')
def main_page():
    return "it's working"


@app.route('/send', methods=['POST', 'GET'])
def send():
    if request.method == 'GET':
        return render_template('count.html')

    try:
        count_of_urls = int(request.form['count'])
    except ValueError:
        return 'ValueError: bad value'

    if count_of_urls <= 150:
        urls = get_urls(count_of_urls)
        # answer = send_requests(urls)
        answer = multi_send(urls)
        return jsonify(answer)
    else:
        return 'Out of range'


if __name__ == '__main__':
    app.run()
