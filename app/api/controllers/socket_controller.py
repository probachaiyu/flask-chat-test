from flask import request
# from flask import session, jsonify
from flask_socketio import emit

from app import app, socketio
from app.api.controllers import application_controller
import pdb

@socketio.on('private chat request', namespace='/chat')
def private_message(message):
    emit('private chat response', {'data': message['data']})

@socketio.on('global chat request', namespace='/chat')
def global_message(message):
    emit('global chat response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/chat')
def connect():
    username = request.args.get('username')
    emit('a user connected', { 'broadcast': "{0} connected".format(username),
        'username': username}, broadcast=True)

@socketio.on('disconnect', namespace='/chat')
def disconnect():
    username = request.args.get('username')
    emit('a user disconnected', { 'broadcast': "{0} disconnected".format(username),
        'username': username}, broadcast=True)
    print('Client disconnected', request.sid)
