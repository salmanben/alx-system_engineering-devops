#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome():
    """
    Route to display a welcome message.

    Returns:
        str: The welcome message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route to display "HBNB".

    Returns:
        str: The string "HBNB".
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    """
    Route to display "C" followed by the value of the text variable.

    Args:
        text (str): The text variable.

    Returns:
        str: The string "C " followed by the value of the text variable.
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python(text='is cool'):
    """
    Route to display "python" followed by the value of the text variable.

    Args:
        text (str): The text variable.

    Returns:
        str: The string "python " followed by the value of the text variable.
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def show_n(n):
    """
    Route to display 'n is a number' only if n is an integer
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(debug=None, port=5000, host='0.0.0.0')
