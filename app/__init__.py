import eventlet
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path="", static_folder="static")
socketio = SocketIO(app)

app.config["MONGODB_DB"] = "chat_test"
app.config["MONGODB_HOST"] = "mongodb://127.0.0.1:27017/chat_test"
app.config["SECRET_KEY"] = "whatitdo"

db = MongoEngine(app)

eventlet.monkey_patch()

from app.api.controllers import *
from app.api.controllers.json import *
