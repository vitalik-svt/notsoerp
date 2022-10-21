import os
import json
from dotenv import load_dotenv

# .env file in root, so get the top up folder
top_up_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../")

# load all env from .env into actual env 
load_dotenv(os.path.join(top_up_folder, ".env"))

class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_CONNECTION_STRING')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('EMAIL_USER')
    MAIL_PASSWORD = os.getenv('EMAIL_PASS')
    APP_USER = os.getenv('APP_USER')
    APP_PASSWORD = os.getenv('APP_PASSWORD')