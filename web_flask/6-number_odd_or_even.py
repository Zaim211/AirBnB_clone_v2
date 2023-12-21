#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
from flask import render_template
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


@app.route('/number/<int:num>', strict_slashes=False)
def is_number(num):
    """
    display "num is a number" only if num is an integer
    """
    return "%d is a number" % num


@app.route('/number_template/<int:num>', strict_slashes=False)
def number_template(num):
    """
    display HTML
    """
    return render_template('5-number.html', num=num)


@app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
def odd_or_even(num):
    """
    display a HTML page only if num is integer
    H1 tag: 'Number: num is even|odd' inside the tag BODY
    """
    return render_template('6-number_odd_or_even.html', num=num)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
