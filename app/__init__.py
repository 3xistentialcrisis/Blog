from flask import Flask
from config import config_options
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


app = Flask(__name__)

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app():

    #Create App Configurations
    app.config.from_object(config_options)

    #Register App Blueprints
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    #Initialise Flask Extensions
    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    return app