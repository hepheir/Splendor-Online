from flask_socketio import SocketIO

from splendor.app.flask import app


socketio = SocketIO(
    app=app,

    # a False setting enables sharing the user session between
    # HTTP routes and Socket.IO events.
    # this will make the app uses Flask’s own session management.
    manage_session=False,

    # The Socket.IO server options
    logger=app.logger,

    # The Engine.IO server configuration
    engineio_logger=app.logger,
    cors_allowed_origins=[],
)
