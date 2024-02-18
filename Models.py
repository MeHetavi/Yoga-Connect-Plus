from Config import app
from flask_login import UserMixin

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hetu@localhost/YC+'

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Users(db.Model, UserMixin):
    __tablename__='users'
    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(12),nullable=False)
    email = db.Column(db.String(100),nullable=False, unique=True)
    name = db.Column(db.String(50),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    gender = db.Column(db.String(7),nullable=False)
    trainer = db.Column(db.Boolean,nullable=False)

    def get_id(self):
        return str(self.username)


with app.app_context():
    db.create_all()