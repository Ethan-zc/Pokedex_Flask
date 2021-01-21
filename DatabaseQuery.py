
from flask import Flask, request, render_template, url_for, redirect, current_app
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

database_controller = Blueprint('database_controller', __name__)
db = SQLAlchemy(database_controller)

@database_controller.route("/cities")
def cities():
    
    res = db.session.execute('select * from cities')
    city_list = res.fetchall()

    return render_template('cities.html', cities=city_list)

