"""Flask config class."""
import os
from common.utils import get_env_variable
from dotenv import load_dotenv
dotenv_path = os.path.realpath('.env')  # Path to .env file
load_dotenv(dotenv_path)

# Postgress global configs
POSTGRES_URL = get_env_variable('DEV_POSTGRES_URL')
POSTGRES_USER = get_env_variable('DEV_POSTGRES_USER')
POSTGRES_PW = get_env_variable('DEV_POSTGRES_PW')
POSTGRES_DB = get_env_variable('DEV_POSTGRES_DB')

# DB_URL formatted accordingly to SQLAlchemy
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)

class Config:
    """Base config vars."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')
    # silence the deprecation warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = DB_URL


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = True
