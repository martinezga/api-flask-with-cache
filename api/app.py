from flask import Flask

from api.configurations import settings
from api.configurations.database import db, cache
from api.routes.user_bp import user_bp
from api.routes.data_populate_bp import data_populate_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings.ApiConfig())
    # initialize DB
    db.init_app(app)
    # create table schema
    with app.app_context():
        import api.models
        db.create_all()
        # Improvement: Implement DB migration
    # initialize Cache
    cache.init_app(app)
    # register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(data_populate_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        host=app.config.get('DB_SERVER'),
        port=app.config.get('PORT'),
        debug=app.config.get('DEBUG'),
    )
