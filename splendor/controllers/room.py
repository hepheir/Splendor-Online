import typing as t

import flask_socketio as sio

from splendor.app import socketio



class Room(sio.Namespace):
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



socketio.on_namespace(Room('/room'))
