"""Flask config class."""
import os
from dotenv import load_dotenv
dotenv_path = os.path.realpath('.env')  # Path to .env file
load_dotenv(dotenv_path)


class Config:
    """Base config vars."""
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME=os.environ.get('SESSION_COOKIE_NAME')


class ProdConfig(Config):
    DEBUG=False
    TESTING=False
    DATABASE_URI=os.environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    ENV="development"
    DEBUG=True
    TESTING=True
    DATABASE_URI=os.environ.get('DEV_DATABASE_URI')
