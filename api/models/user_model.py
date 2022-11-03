from api.configurations.database import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.db.Column(
        db.Integer,
        primary_key=True,
    )
    name = db.Column(
        db.String(32),
    )
    lastname = db.Column(
        db.String(32),
    )
    email = db.Column(
        db.String(64),
        unique=True
    )

    def __init__(self, name, lastname, email):
        self.name = name
        self.lastname = lastname
        self.email = email
