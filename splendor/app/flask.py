import os
import logging

from flask import Flask


app = Flask(__name__)

app.config["SECRET_KEY"] = os.urandom(16)
app.logger.setLevel(logging.INFO)
app.logger.setLevel(logging.INFO)
