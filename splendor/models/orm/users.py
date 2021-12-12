from flask_login.mixins import UserMixin

from splendor.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Text, primary_key=True)
    user_pw = db.Column(db.Text, nullable=False)

    room_id = db.Column(db.Text, db.ForeignKey('rooms.room_id'), default='/lobby')

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return self.get_id()

    def get_id(self) -> str:
        return self.user_id
