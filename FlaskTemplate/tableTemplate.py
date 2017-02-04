#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
    stocks = {
        'IBM': 146.48,
        'MSFT': 44.11,
        'CSCO': 25.54,
    }
    return render_template('result.html', result = stocks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
