import logging
from flask import Flask
from flask.logging import default_handler
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

# This will be available throughout the app without direct access to the app instance
server_carrier = None

# class to access server and it restricts direct access of server
class Server:
    def __init__(self, app):
        self.server = app

    def get_server(self):
        return self.server

    def set_server(self, app):
        self.server = app


def register_blueprints(app):
    from .attach_route_via_blueprint import attach_route_via_blueprint
    attach_route_via_blueprint(app)


def attach_routes(app):
    from .routes.main import attach_routes
    attach_routes(app)
    

def initiate_app():
    """Create a Flask app
    """
    # Instantiate logger
    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    default_handler.setFormatter(formatter)
    root_logger.addHandler(default_handler)

    # Create app instance
    app = Flask(__name__)

    # assign value to class local variable which can't be accessed directly and it can be access using Server().get_server() throughout the app
    global server_carrier
    server_carrier = Server(app)

    # now the env variables are assible using app.config.get('ENV_VAR_NAME')
    app.config.from_object("src.config.settings")

    CORS(app, supports_credentials=True)

    # attach routes using blueprints
    # attach_routes(app)
    register_blueprints(app)

    return app