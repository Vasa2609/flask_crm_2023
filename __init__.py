import os
from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

from . import routes