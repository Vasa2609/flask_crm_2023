from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, IntegerField



class LoginForm(FlaskForm):
    username = SubmitField("Username")
    password = PasswordField("Password")
    remember = BooleanField("Remember me")
    submit = SubmitField("Submit")

class Studentform(FlaskForm):
    name = StringField("Name")
    username = StringField("Username")
    age = IntegerField("Age")
    home_address = StringField('home adress')
    group_id = IntegerField("Group")
    submit = SubmitField("Submit")