from flask import Flask
from .extensions import db
from .routes.main import main


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Регистрируем Blueprints
    app.register_blueprint(main.main)

    return app
