import flask

from splendor.app import app
from splendor.app import socketio


socketio.on('connection')
def connection():
    ip = flask.request.environ.get('HTTP_X_REAL_IP', flask.request.remote_addr)
    app.logger.info(f'New connection from {ip}')


@socketio.on('message')
def on_message(data):
    app.logger.info(data)
