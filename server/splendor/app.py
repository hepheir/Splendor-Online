# -*- coding: utf-8 -*-

import typing as t

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO


app = Flask(__name__)
app.config["SECRET_KEY"] = "tmp_secret_key"

CORS(app)
socketio = SocketIO(app)


def run(
    host: t.Optional[str] = None,
    port: t.Optional[int] = None,
    debug: t.Optional[bool] = None,
    load_dotenv: bool = True,
    **options: t.Any,
) -> None:
    """Runs the application on a local development server."""
    socketio.run(
        app, host, port, debug=debug, load_dotenv=load_dotenv, **options
    )
