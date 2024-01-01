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


if __name__ == '__main__':
    app.run(debug=None, port=5000, host='0.0.0.0')
