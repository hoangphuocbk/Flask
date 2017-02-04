#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<user_name>')
def index(user_name):
    return render_template('hello.html', name = user_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
