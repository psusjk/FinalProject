from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

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

    from .table import Customer,Manager

    create_database(app)   

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