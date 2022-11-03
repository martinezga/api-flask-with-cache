from decouple import config
from faker import Faker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from api.models.user_model import UserModel


def populate_data(db: SQLAlchemy):
    """Dynamic Data population"""
    # Get users count first and compare with data records expected

    DATA_RECORDS_QTY = config('DATA_RECORDS_QTY', default=100, cast=int)
    users_qty = UserModel.query.count()

    if users_qty < DATA_RECORDS_QTY:
        users_to_insert = DATA_RECORDS_QTY - users_qty
        fake = Faker(use_weighting=False)

        for _ in range(users_to_insert):
            name = fake.first_name()
            lastname = fake.last_name()
            email = f'{name.lower()}{lastname.lower()}{fake.pyint()}@email.com'
            user = UserModel(name, lastname, email)
            try:
                db.session.flush()
                db.session.add(user)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                continue
