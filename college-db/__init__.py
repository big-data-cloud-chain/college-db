import os

from flask import Flask, redirect


def create_app(test_config=None):
    # create and configure the college-db
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
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

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # redirect to login page
    @app.route('/')
    def redirect_to_login():
        return redirect('auth/login')

    return app