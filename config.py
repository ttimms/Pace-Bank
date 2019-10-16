import os
baseDir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Secret key used by flask-wtf to generate csrf token.
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_PATH') or 'sqlite:///' + os.path.join(baseDir, 'PaceApp.db')
    # Track modifications currently disabled to avoid overhead.
    SQLALCHEMY_TRACK_MODIFICATIONS = False