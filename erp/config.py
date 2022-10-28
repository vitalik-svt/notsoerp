import os
from dotenv import load_dotenv

# .env file in root, so get the top up folder
top_up_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../")

# load all env from .env into actual env 
load_dotenv(os.path.join(top_up_folder, ".env"))

class Config:
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@pgdb:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')

    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    MAIL_USE_TLS = True if os.getenv('MAIL_USE_TLS').lower() == 'true' else False

    APP_USER = os.getenv('APP_USER')
    APP_PASSWORD = os.getenv('APP_PASSWORD')
    APP_USER_MAIL = os.getenv('APP_USER_MAIL')
    APP_DEBUG_MODE = True if os.getenv('APP_DEBUG_MODE').lower() == 'true' else False