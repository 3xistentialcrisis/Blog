from flask import Flask
from config import Config
from flask_mail import Mail
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_uploads import IMAGES, UploadSet,configure_uploads


db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)

def create_app():
    app = Flask(__name__)
    #Create App Configurations
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'paper'

    #Register App Blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Initialise Flask Extensions
    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    configure_uploads(app, photos)
    mail.init_app(app)

    return app