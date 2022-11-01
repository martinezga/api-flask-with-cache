from flask import Flask

from configurations import settings
from configurations.database import db, custom_init_db
from routes.user_bp import user_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings.ApiConfig())
    # initialize DB
    db.init_app(app)
    # create table schema
    with app.app_context():
        import models
        db.create_all()
    # Custom logic
    custom_init_db()
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
