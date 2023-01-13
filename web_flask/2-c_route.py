#!/usr/bin/python3
from flask import Flask
"""
Starting a 'hello world' application
"""

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    """
    displays hello world
    """
    return f'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    display HBNB
    """
    return 'HBNB'


app.route('/c/<text>', strict_slashes= False)
def c(text):
"""
display c followed by the value of <text>
"""
    text.replace('_', ' ')
    return f'C{text}'



if __name__ == '__main__':
    app.run(host='0.0.0.0')
