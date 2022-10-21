from erp import Config
from erp.models.service import User
from erp import db

def init_user(username, email, password):

    # create user in database

    user = User(username=username
                , email=email
                , password=password)
    db.session.add(user)
    db.session.commit()

