from flask import redirect
from flask import send_from_directory

from splendor.app import app


@app.get('/')
def index():
    return redirect('/index.html')


@app.get('/<path:path>')
def path(path):
    return send_from_directory('../static', path)
