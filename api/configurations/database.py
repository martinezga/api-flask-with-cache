from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def custom_init_db():
    # Dynamic Data population
    # Get users count first and compare with data records expected
    from decouple import config
    DATA_RECORDS_QTY = config('DATA_RECORDS_QTY', default=100, cast=int)
