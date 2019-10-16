from flask import Flask
from config import Config

PaceApp = Flask(__name__)
PaceApp.config.from_object(Config)

from PaceApp import routes
