from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, TextAreaField, SubmitField

class LoginForm(FlaskForm):
   username = StringField('Username', [validators.InputRequired()])
   password = PasswordField('Password', [validators.InputRequired()])

class ContactForm(FlaskForm):
  name = StringField("Name")
  email = StringField("Email")
  subject = StringField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send") 