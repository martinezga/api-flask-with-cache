from sqlalchemy import func

from api.configurations.database import db


class AuditModel(db.Model):
    __abstract__ = True
    created = db.Column(
        db.DateTime,
        default=func.now(),
    )
    updated = db.Column(
        db.DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
