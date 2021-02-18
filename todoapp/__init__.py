from flask import Flask
from .main.routes import main


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'this-too-shall-pass'

    app.register_blueprint(main)

    app.run()
    # return app
