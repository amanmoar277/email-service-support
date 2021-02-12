import smtplib
from flask import Blueprint, make_response, jsonify, request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def attach_routes(app):
    """Attach routes to app_instance"""
    
    @app.route("/", methods=["GET"])
    def base():
        return "<center><h1><div style=""margin-top:40vh"">Welcome to our server !!</div></h1></center>"
    
    @app.route("/health", methods=["GET"])
    def health():
        return make_response(jsonify({"status": 200, "data": {"message": "app is running!"}}))

    @app.route("/send-email", methods=["POST"])
    def send_email():
        message = MIMEMultipart()
        sender = request.args.get('from')
        receiver = request.args.get('to')
        body = request.args.get('body')
        subject = request.args.get('subject')
        isHTML = request.args.get('isHTML')

        if sender is None or receiver is None:
            return make_response(jsonify({"status": 421, "data": 'Required fields are not provided'}))

        p = os.path.abspath('../utils/main.py')
        from p import send_email


        try:
            send_email({sender, receiver, body, password, subject, isHTML})
       
        except Exception as e:
            return make_response(jsonify({"status": 500, "data": 'Email Sending failed'}))

        return make_response(jsonify({"status": 200, "data": 'Email Sent Successflly'}))


