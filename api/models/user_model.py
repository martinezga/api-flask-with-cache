from typing import Dict

from api.configurations.database import db
from api.models.audit import AuditModel


class UserModel(AuditModel):
    __tablename__ = 'users'
    id = db.Column(
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

    @staticmethod
    def filtered_users(filter_fields: Dict = None):
        # By default, return untouched query
        base_query = UserModel.query
        if filter_fields:
            for key, value in filter_fields.items():
                attr = getattr(UserModel, key)
                # Improvement: non-case sensitive filter
                base_query = base_query.filter(attr == value)

        return base_query
