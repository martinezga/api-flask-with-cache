from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from configurations.settings import ApiConfig

engine = create_engine(ApiConfig.SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.
    import models
    Base.metadata.create_all(bind=engine)

    # Dynamic Data population
    # Get users count first and compare with data records expected
    from decouple import config
    DATA_RECORDS_QTY = config('DATA_RECORDS_QTY', default=100, cast=int)
