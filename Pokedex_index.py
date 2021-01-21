from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from flask import Blueprint
import json

pokedex_index = Blueprint('pokedex_index', __name__)

@pokedex_index.route("/index")
def index():

    return render_template('index.html')