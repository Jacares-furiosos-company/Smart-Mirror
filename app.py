from flask import Flask, render_template, redirect, url_for
import requests as requests
import json

from Classes import validacaoInternet

app = Flask(__name__)


@app.route('/')
def offNetwork():
    validacaoInternet.internet()

    url = "http://www.kite.com/"
    timeout = 5

    try:
        requests.get(url, timeout=timeout)
        return redirect('/index')
    except (requests.ConnectionError, requests.Timeout) as exception:
        return render_template('offNetwork.html', myFunction=offNetwork)


@app.route('/index')
def index():
    return render_template('indexFeia.html')


if __name__ == '__main__':
    app.run()
