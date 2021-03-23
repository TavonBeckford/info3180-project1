import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://lchkowtajeitzh:3850078e84a7fdc62f093f769faa92db2aac926558a86d5aa04e957e1125d859@ec2-54-161-239-198.compute-1.amazonaws.com:5432/dcl8ouskihpmb0'
    SQLALCHEMY_TRACK_MODIFICATIONS = True # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = './app/static/uploads'

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False