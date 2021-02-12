import smtplib
from flask import Blueprint, make_response, jsonify, request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email({sender, receiver, body, password, subject, isHTML,}):
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

    server.login(message['From'], '20sss15@Adddd')
    server.sendmail(message['From'], receiver, msg.as_string())
    server.quit()

    try:
        server.login(message['From'], password)
        server.sendmail(message['From'], receiver, msg.as_string())
        server.quit()
    
    except Exception as e:
        return make_response(jsonify({"status": 500, "data": {"loaded_flows": []}}))

    return make_response(jsonify({"status": 200, "data": {"loaded_flows": []}}))