from flask import Flask

from configurations import settings
from configurations.database import init_db, db_session
from routes.user_bp import user_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings.ApiConfig())
    # initialize SQLAlchemy - https://flask.palletsprojects.com/en/2.2.x/patterns/sqlalchemy/#declarative
    init_db()
    # Improvement: Implement DB migration

    # register blueprints
    app.register_blueprint(user_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        host=app.config.get('DB_SERVER'),
        port=app.config.get('PORT'),
        debug=app.config.get('DEBUG'),
    )

    # Remove database sessions at the end of the request or when the application shuts down
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
