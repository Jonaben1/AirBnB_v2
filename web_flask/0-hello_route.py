#!/usr/bin/python3
from flask import Flask

"""
Starting a 'Hello World' flask application'
"""
app = Flask(__name__)

@app.route(''/', strict_slashes=False)
def hello_world():
"""
displays 'hello HBNB!'
"""
    return f'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
