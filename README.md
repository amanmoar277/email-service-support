# email_service
Python service to send email


Install specific version of pip which is on Heroku
```
References:
1. https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524
2. https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0<br />
```
<br />

#### 1. To add specific version of pip
```
python3 get-pip.py pip==20.1.1
```
Use
```
python3 -m pip freeze > requirements.txt
```
if
```
pip freeze > requirements.txt
```
does not work
<br />
<br />
#### 2. To add modul
```
pip install flask_wtf
```
<br />

#### 3. To run locally
```
python3 main.py
```
OR
```
export FLASK_APP=email_service
export FLASK_ENV=development
flask run
```
<br />

#### While deplying on heroku
```
web: gunicorn main:server
```
and this server variable must be present in main.py
<br />
<br />
### To use this service

URL: https://email-service-support.herokuapp.com/send-email <br />
REQUEST TYPE: POST<br />
REQUEST Body: <br />
```
{
	"from": "sender_email",
	"to": "receiver_email",
	"isHTML": true,  ( or false)
	"subject": "email_subject_here",
	"body": "<center><h1><div style=margin-top:10vh>Hey, I hope you are doing great!!</div></h1></center>",
	"password": "from_email_pass_here"
}
```

### Note:
##### 1. Pass body in HTML tag in request if required
```
<center><h1><div style=margin-top:10vh>Hey, I hope you are doing great!!</div></h1></center>
```
