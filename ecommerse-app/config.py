import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cambia-esta-clave-por-una-segura'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:zzzsql17@localhost:5432/ecommerse'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
