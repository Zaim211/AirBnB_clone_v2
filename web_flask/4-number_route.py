#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """
    returns the message to display in our browser
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    display "HBNB" in the browser
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def Cisfun(text):
    """
    display "C" followed by the value of the text variable
    """
    string = 'C %s' % text
    return string.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def Pytho(text):
    """
    display "Python", followed by the value of text variable
    """
    string = 'Python %s' % text
    return string.replace('_', ' ')


@app.route('/number/<int:number>', strict_slashes=False)
def is_number(number):
    """
    display "number is a number" only if number is an integer
    """
    return "%s is a number" % number

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
