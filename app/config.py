import os

class Config:
    SECRET_KEY = 'abcdefghijklmnopqrstuvwxyz'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://flask:flask@db:5432/flaskdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False