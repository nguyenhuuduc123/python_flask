from flask import Flask
from models.home_model import db
from flask_migrate import Migrate
from events import socketio

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    migrate.init_app(app, db)
    app.config['SECRET_KEY'] = 'secret!'
    with app.app_context():
        from controllers import home_controller
        app.register_blueprint(home_controller.bp)
    socketio.init_app(app)
    return app