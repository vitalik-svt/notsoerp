from erp import create_app, db, Config
from erp.models.init_db import init_db
from erp.service.users import init_user
import argparse


# create possibility to launch py from cli with arguments
parser = argparse.ArgumentParser()
parser.add_argument('--init_db', '-idb', action='store_true', help='create db if dont exist')
parser.add_argument('--init_user', '-iu', action='store_true', help='create db if dont exist')
parser.add_argument('--debug', '-d', action='store_true', help='launch flask in debug mode')
args = parser.parse_args()


# actually creating flask app
app = create_app()


if __name__ == '__main__':

    if args.init_db:
        init_db(app=app, db=db)
    if args.init_user:
        init_user(username=Config.APP_USER
                , email=Config.MAIL_USERNAME
                , password=Config.APP_USER)

    # actually running app
    app.run(host="0.0.0.0", port = 8000, debug=args.debug)