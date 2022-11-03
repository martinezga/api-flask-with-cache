from flask import Flask

from api.configurations import settings
from api.configurations.data_population import populate_data
from api.configurations.database import db
from api.routes.user_bp import user_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings.ApiConfig())
    # initialize DB
    db.init_app(app)
    # create table schema
    with app.app_context():
        import api.models
        db.create_all()
        # Custom logic to populate data
        populate_data(db)
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
