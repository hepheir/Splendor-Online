# -*- coding: utf-8 -*-

import typing as t

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "tmp_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"


CORS(app)
db = SQLAlchemy(app)
socketio = SocketIO(app)


@app.teardown_request  # type: ignore
def shutdown_session(exception=None):
    db.session.remove()


def run(
    host: t.Optional[str] = None,
    port: t.Optional[int] = None,
    debug: t.Optional[bool] = None,
    load_dotenv: bool = True,
    **options: t.Any,
) -> None:
    """Runs the application on a local development server."""
    db.create_all()
    socketio.run(
        app, host, port, debug=debug, load_dotenv=load_dotenv, **options
    )
