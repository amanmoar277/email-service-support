import smtplib
from functools import wraps
from flask import Blueprint, make_response, jsonify, request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src import server_carrier
from src.utils.db import connect_to_db, DatabaseTypes, DatabaseNames, Collections

def get_defaut_collection():
    server = server_carrier.get_server()
    uri = server.config.get('MONGODB_URI')
    db_conn = connect_to_db(DatabaseTypes.MONGODB, uri, DatabaseNames.python_test_db.value)
    member_coll = db_conn.get_collection(Collections.member.value)
    return member_coll

def send_email(sender, receiver, body, password, subject, isHTML):
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    
    if isHTML is not True:
        message.attach(MIMEText(body, 'plain'))
    else:
        message.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        app = server_carrier.get_server()
        # print(password or app.config.get('SECRET_KEY'))
        server.login(message['From'], password)
        server.sendmail(message['From'], receiver, message.as_string())
        server.quit()
    
    except NameError as e:
        logging.info('Error->',e)
        return False

    return True

def retrieve_request_parameters():
    """It is a decorator Python file that retreive request
    parameter from post and get request.
    """
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            kwargs.update({'request_method': request.method})
            try:
                query_parameters = request.args.to_dict()
                kwargs['query_parameters'] = query_parameters
                if request.method == "GET":
                    parameters = query_parameters
                    kwargs.update(parameters)
                elif request.method == "POST" or request.method == "PUT" and request.content_type:
                    content_types = request.content_type.split(';')
                    if "application/json" in content_types and isinstance(
                            request.json, dict) and any(request.json):
                        kwargs.update(request.json)
            except Exception as exception:
                print(
                    f'JSON format is not done properly for filter {str(exception)}'
                )
                raise ValueError("Check Query Params")

            return func(*args, **kwargs)
        return inner
    return wrapper

def parse_json(data):
    return json.loads(json_util.dumps(data))