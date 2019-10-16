from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

PaceApp = Flask(__name__)
PaceApp.config.from_object(Config)
db = SQLAlchemy(PaceApp)
migrate = Migrate(PaceApp, db)

from PaceApp import routes, dbModels
