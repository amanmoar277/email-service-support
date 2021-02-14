import os
# import smtplib
import logging
# from pymongo import MongoClient
from flask import make_response, jsonify, request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ..utils.main import retrieve_request_parameters, get_defaut_collection         
# from src.utils.db import connect_to_db, DatabaseTypes, DatabaseNames, Collections

def attach_routes(app):
    """Attach routes to app_instance"""
    
    @app.route("/", methods=["GET"])
    def base():
        return "<center><h1><div style=""margin-top:40vh"">Welcome to our server !!</div></h1></center>"
    
    @app.route("/health", methods=["GET"])
    def health():
        return make_response(jsonify({"status": 200, "data": {"message": "app is running!"}}))

    @app.route("/api/data", methods=["GET"])
    def get_data():

        member_coll = get_defaut_collection()
        try:
            member_data = list(member_coll.find(
                filter={
                    "status": 1
                },
                limit=100,
                sort=[("_id", -1)],
                projection={"_id": 1, "name": 1, 'status': 1}
            ))            

            html = "<div><center style=""margin-top:40vh""><table><tr><th>Name</th><th>Status</th></tr>"
            for member in member_data:
                html += f"<tr><th>{member.get('name')}</th><th>{member.get('status')}</th></tr>"
            html += "<table></center></div>"
            return html

            # return make_response(jsonify({"status": 200, "data": {"message": "data fetched successfully", "data": member_data}}))
        except Exception as err:
            logging.info('Error while fetching data')
            return make_response(jsonify({"status": 500, "error": {"message": "data fetched failed", "error": err}}))

    @app.route("/api/data", methods=["POST"])
    @retrieve_request_parameters()
    def post_data(**kwargs):
        name = kwargs.get('name')
        status = kwargs.get('status')
        data = {
            "name": name,
            "status": status,
        }

        member_coll = get_defaut_collection()
        try:
            member_data = member_coll.insert_one(data)
            logging.info('Data saved successfully')
            return make_response(jsonify({"status": 200, "data": {"message": "data saved successfully"}}))
        except Exception as err:
            logging.info('Error while saving data')
            return make_response(jsonify({"status": 500, "error": {"message": "data saving failed", "error": err}}))
            

    @app.route("/send-email", methods=["POST"])
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

    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')    
    def all(path):
        return "<center><h1><div style=""margin-top:40vh"">Bro, nothing on this route!!</div></h1></center>"


