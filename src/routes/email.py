import logging
from flask import Blueprint, make_response, jsonify
from email.mime.multipart import MIMEMultipart
from ..utils.main import retrieve_request_parameters, get_defaut_collection         

api_email_blueprint = Blueprint('api_email', __name__)


@api_email_blueprint.route("/send", methods=["POST"])
@retrieve_request_parameters()
def send_email(**kwargs):
    # print(kwargs)
    message = MIMEMultipart()
    sender = kwargs.get('from')
    receiver = kwargs.get('to')
    body = kwargs.get('body')
    subject = kwargs.get('subject')
    isHTML = kwargs.get('isHTML')
    password=kwargs.get('password')

    if sender is None or receiver is None or password is None:
        return make_response(jsonify({"status": 421, "data": 'Required fields are not provided'}))

    try:
        from ..utils.main import send_email
        result = send_email(sender, receiver, body, password, subject, isHTML)
    
    except Exception as e:
        return make_response(jsonify({"status": 500, "error": e, "data": 'Email Sending failed'}))

    if result is True:
        return make_response(jsonify({"status": 200, "data": 'Email Sent Successflly'}))
    return make_response(jsonify({"status": 500, "error": {"message": 'Email Sending failed!!'}}))


