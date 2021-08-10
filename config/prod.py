import os
DEBUG = False
SECRET_KEY = 'topsecret'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False

#DEBUG = True
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/postgres'
#SQLALCHEMY_TRACK_MODIFICATIONS = False