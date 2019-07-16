from datetime import datetime
from app import _db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(_db.Model, UserMixin):
    id = _db.Column(_db.Integer, primary_key=True)
    username = _db.Column(_db.String(20), unique=True, nullable=False)
    email = _db.Column(_db.String(120), unique=True, nullable=False)
    image_file = _db.Column(_db.String(20), default='default.jpg')
    password = _db.Column(_db.String(60), nullable=False)
    posts = _db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(_db.Model):
    id = _db.Column(_db.Integer, primary_key=True)
    title = _db.Column(_db.String(100), nullable=False)
    date_posted = _db.Column(_db.DateTime, nullable=False, default=datetime.utcnow)
    content = _db.Column(_db.Text, nullable=False)
    user_id = _db.Column(_db.Integer, _db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"
