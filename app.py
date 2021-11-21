from flask import Flask, render_template
import requests as requests
import json

from Classes import validacaoInternet

app = Flask(__name__)


@app.route('/inativo')
def distancia():
    distacia1 = 40
    if (distacia1 <= 40):
        return render_template('index.html')

    return render_template('inativo.html')


@app.route('/')
def offNetwork():
    validacaoInternet.internet()

    url = "http://www.kite.com/"
    timeout = 5

    try:
        requests.get(url, timeout=timeout)
        return distancia()
    except (requests.ConnectionError, requests.Timeout) as exception:
        return render_template('offNetwork.html', myFunction=offNetwork)


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
