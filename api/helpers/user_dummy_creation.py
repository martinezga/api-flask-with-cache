from faker import Faker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError


from api.models.user_model import UserModel


def create_dummy_user(db: SQLAlchemy, records_qty=0):
    """Dynamic dummy user population"""
    created_users = 0
    fake = Faker(use_weighting=False)

    for _ in range(records_qty):
        name = fake.first_name()
        lastname = fake.last_name()
        email = f'{name.lower()}{lastname.lower()}{fake.pyint()}@email.com'
        user = UserModel(name, lastname, email)
        try:
            db.session.flush()
            db.session.add(user)
            db.session.commit()
            created_users += 1
        except IntegrityError:
            db.session.rollback()
            continue

    users_qty = UserModel.query.count()

    return created_users, users_qty
