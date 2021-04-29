from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()
DB_NAME = "database.db"


def run_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'This is Sumit Kumar'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .home import homewindow
    from .auth import auth

    app.register_blueprint(homewindow, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .table import Customer, Manager

    create_database(app)

    with app.app_context():
        if len(Manager.query.all()) < 4:
            manager = Manager(
                loginName='sumit1',
                password=generate_password_hash("password", method='sha256'),
                fullName="Sumit",
                phoneNumber=5404495670,
                address="1900 Lane Foxhunt"
            )
            db.session.add(manager)
            db.session.commit()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(loginName):
        return Customer.query.get(str(loginName))

    return app


def create_database(app):
    if not path.exists('webpages/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
