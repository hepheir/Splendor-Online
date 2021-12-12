import typing as t

import flask_socketio as sio

from splendor.app import socketio


class Lobby(sio.Namespace):
    def on_connect(self, sid, environ):
        pass

    def on_disconnect(self, sid):
        pass

    def on_message(self, message):
        sio.send(message)

    def on_join(self, data: t.Dict):
        user_id = data.get('user_id')
        room_id = data.get('room_id')

        sio.join_room(room_id)
        sio.send(f'{user_id} has entered the room.', to=room_id)

    def on_leave(self, data: t.Dict):
        user_id = data.get('user_id')
        room_id = data.get('room_id')

        sio.leave_room(room_id)
        sio.send(f'{user_id} has left the room.', to=room_id)


socketio.on_namespace(Lobby('/lobby'))
