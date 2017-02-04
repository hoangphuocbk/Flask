#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<int:score>')
def score(score):
    return render_template('hello_condition.html', marks = score)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
