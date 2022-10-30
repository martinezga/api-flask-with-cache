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
