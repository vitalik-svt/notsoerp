from erp import create_app, db, Config
from erp.models.init_db import init_db


# actually creating flask app
app = create_app()


if __name__ == '__main__':

    init_db(app=app, db=db)

    # actually running app
    app.run(host="0.0.0.0", port = 8000, debug=Config.APP_DEBUG_MODE)