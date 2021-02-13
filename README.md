# email_service
Python service to send email




Install spectfic version of pip which is on Heroku

Reference-> https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524
https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0

To add specific version of pip to
python3 get-pip.py pip==20.1.1


Use
python3 -m pip freeze > requirements.txt
if 
pip freeze > requirements.txt
does not work


To add modulest
pip install flask_wtf


To run locally
python3 main.py

OR

export FLASK_APP=email_service
export FLASK_ENV=development
flask run


While deplying on heroku
web: gunicorn main:server
and this server variable must be present in main.py



# To use this service

URL: https://email-service-support.herokuapp.com/send-email
REQUEST TYPE: POST
REQUEST Body: 
{
	"from": "amanmoar.nit.kkr@gmail.com",
	"to": "amanmoar.nit.kkr@gmail.com",
	"isHTML": true,
	"subject": "test",
	"body": "<center><h1><div style=margin-top:40vh>Bro, nothing on this route!!</div></h1></center>",
	"password": "from_email_pass_here"
}


