from flask import Flask

from routes.user_bp import user_bp
from configurations import settings

from models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings.ApiConfig())
    # initialize SQLAlchemy
    # db.init_app(app)

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
