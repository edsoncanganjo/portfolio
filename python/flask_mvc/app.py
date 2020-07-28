from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import app_config, app_active

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(app_config[app_active])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    db = SQLAlchemy(app)
    db.init(app)

    @app.route('/')
    def index():
        return 'Olá, Edson Canganjo!'


    return app

