#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    """Render states list in html page"""
    states = storage.all()
    return render_template('7-state_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """Remove current SQLalchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
