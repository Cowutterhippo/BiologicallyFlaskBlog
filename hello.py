import os
from flask import app
from flask_mail import flask_mail

mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com' app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

