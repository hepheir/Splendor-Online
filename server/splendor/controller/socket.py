from splendor.app import socketio


@socketio.on('connect')
def handle_connect(json):
    print('CONNECT')



@socketio.on('message')
def handle_message(json):
    socketio.emit('message', json, broadcast=True)
