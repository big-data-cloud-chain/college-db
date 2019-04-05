import os

from flask import Flask, redirect, url_for


def create_app(test_config=None):
    # create and configure the college-db
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'college.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .auth import auth
    app.register_blueprint(auth)

    from .dashboard import dashboard
    app.register_blueprint(dashboard)
    app.add_url_rule('/', endpoint='dashboard/index')

    # Registers the database with the application
    from .db import init_app
    init_app(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # redirect to login page

    return app
