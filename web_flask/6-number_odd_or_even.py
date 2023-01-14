#!/usr/bin/python3
from flask import Flask
from flask import render_template
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

app.route('/python/(<text>)', strict_slashes=False)
def python(text='is cool'):
    """
    display python followed by the value of text
    """
    text.replace('_','')
    return f'Python{text}'

app.route('/number/<n>', strict_slashes=False)
def number(n):
    """
    display n only if n is an integer
    """
    if type(n) == int:
        return f'Number{n}'

@app.route('/number_template/<n>', strict_slashes=False)
def number_templates(n):
    """
    display html template if n is an int
    """
    if type(n) == int:
        render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    display html if n is an integer
    check whetherbn is odd or even
    """
    if type(n) == int:
        return render_template('6-number_odd_or_even.html', n=n)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
