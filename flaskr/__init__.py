import os

from flask import Flask


def create_app():
    # create the app
    # instance_relative_config tells the app that configuration files are relative to the instance folder
    app = Flask(__name__, instance_relative_config=True)

    # configurate the app
    app.config.from_mapping(
        # secret key to keep data safe, should be changed later
        SECRET_KEY='dev',
        # path to the database
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    @app.route('/', methods=('GET', 'POST'))
    def page_default():
        return 'hewofddd'

    @app.route('/eo')
    def page_eo():
        return 'harambe'

    # initializes database's functionalities
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
