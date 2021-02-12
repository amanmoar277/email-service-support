from flask import Flask
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

def attach_routes(app):
    from .routes.main import attach_routes
    attach_routes(app)
    
def initiate_app():
    """Create a Flask app
    """
    app = Flask(__name__)

    CORS(app, supports_credentials=True)

    attach_routes(app)

    return app