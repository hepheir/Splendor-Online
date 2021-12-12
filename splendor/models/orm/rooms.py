from splendor.app import db


class Room(db.Model):
    __tablename__ = 'rooms'

    room_id = db.Column(db.Text, primary_key=True)


room = Room(room_id='/lobby')
db.session.add(room)
db.session.commit()
