from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO


app = Flask(__name__)
cors = CORS(app, resources={
    r"*": {"origins": "*"},
})

socketio = SocketIO(app, cors_allowed_origins="*")
