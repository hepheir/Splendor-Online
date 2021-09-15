# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO


app = Flask(__name__)
app.config["SECRET_KEY"] = "tmp_secret_key"

CORS(app)
socketio = SocketIO(app)


run = socketio.run
