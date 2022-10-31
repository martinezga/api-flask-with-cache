from sqlalchemy import Column, Integer, String
from configurations.database import Base


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(
        Integer,
        primary_key=True,
    )
    name = Column(
        String(32),
    )
    lastname = Column(
        String(32),
    )
    email = Column(
        String(64),
        unique=True
    )

    def __init__(self, name, lastname, email):
        self.name = name
        self.lastname = lastname
        self.email = email
