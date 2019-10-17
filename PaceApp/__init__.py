from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

PaceApp = Flask(__name__)
PaceApp.config.from_object(Config)

db = SQLAlchemy(PaceApp)
migrate = Migrate(PaceApp, db)

login = LoginManager(PaceApp)
login = LoginManager(PaceApp)
login.login_view = 'login'

from PaceApp import routes, dbModels
