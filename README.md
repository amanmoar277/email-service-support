# email_service
Python service to send email<br />
<br />
<br />
<br />
<br />
Install spectfic version of pip which is on Heroku<br />
<br />
Reference-> https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524<br />
https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0<br />
<br />
##### To add specific version of pip to<br />
python3 get-pip.py pip==20.1.1<br />
<br />
<br />
Use<br />
python3 -m pip freeze > requirements.txt<br />
if <br />
pip freeze > requirements.txt<br />
does not work<br />
<br />
<br />
##### To add modulest<br />
pip install flask_wtf<br />
<br />
<br />
##### To run locally<br />
python3 main.py<br />
<br />
OR<br />
<br />
export FLASK_APP=email_service<br />
export FLASK_ENV=development<br />
flask run<br />
<br />
<br />
##### While deplying on heroku<br />
web: gunicorn main:server<br />
and this server variable must be present in main.py<br />
<br />
<br />
<br />
### To use this service<br />

URL: https://email-service-support.herokuapp.com/send-email <br />
REQUEST TYPE: POST<br />
REQUEST Body: <br />
{<br />
	"from": "sender_email",<br />
	"to": "receiver_email",<br />
	"isHTML": true,  ( or false)<br />
	"subject": "email_subject_here",<br />
	"body": "Hey, I hope you are doing great!!",<br />
	"password": "from_email_pass_here"<br />
}<br />

### Note:
1. Pass body in HTML tag in request
E.g. -> <center><h1><div style=margin-top:40vh>Bro, nothing on this route!!</div></h1></center>
