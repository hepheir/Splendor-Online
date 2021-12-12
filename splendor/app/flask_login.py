import typing as t

from flask_login import LoginManager

from splendor.app.flask import app


login_manager = LoginManager()
login_manager.init_app(app)


# Below codes are implemented only for typing perpose.
# these won't be available on runtime.
if t.TYPE_CHECKING:
    # Typing hits for Flask-Login
    from flask_login import AnonymousUserMixin
    from flask_login import UserMixin
    current_user: t.Union[UserMixin, AnonymousUserMixin]
