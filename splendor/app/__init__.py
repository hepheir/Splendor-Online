from splendor.app.flask import app
from splendor.app.flask_login import login_manager
from splendor.app.flask_socketio import socketio
from splendor.app.flask_sqlalchemy import db


def run(*args, **kwargs) -> None:
    socketio.run(app, *args, **kwargs)
