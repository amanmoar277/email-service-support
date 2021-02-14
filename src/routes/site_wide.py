from flask import Blueprint, make_response, jsonify

api_default_blueprint = Blueprint('api_default', __name__)

    
@api_default_blueprint.route("/", methods=["GET"])
def base():
    return "<center><h1><div style=""margin-top:40vh"">Welcome to our server !!</div></h1></center>"

@api_default_blueprint.route("/health", methods=["GET"])
def health():
    return make_response(jsonify({"status": 200, "data": {"message": "app is running!"}}))

@api_default_blueprint.route('/', defaults={'path': ''})
@api_default_blueprint.route('/<path:path>')    
def all(path):
    return "<center><h1><div style=""margin-top:40vh"">Bro, nothing on this route!!</div></h1></center>"
