
from flask import Flask, request, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from PokemonApi import pokemon_api
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Pokedex_test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecret'
db = SQLAlchemy(app)

class Pokemons(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique = True)
    description = db.Column(db.String(300))
    uniquemove = db.Column(db.String(20))
    location = db.Column(db.String(50))
    type = db.Column(db.String(20))
    image = db.Column(db.String(100), unique = True)

class users_pokemons(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    pokemon = db.Column(db.String(20))

@app.route('/pokemonfetch')
def pokemonfetch():
    #username = request.args.get('username')
    username = "skors004"
    userPokemon = users_pokemons.query.filter_by(username = username).first()
    rows = userPokemon.execute().fetchall()
    for row in rows:
        pokefetch = Pokemons.query.filter_by(name = row.pokemon).first()
        if pokefetch:
            print("Found it")
            return("Found the Pokemon")
    print("Not there :(")
    return("Did not find the pokemon")
    
if __name__=="__main__":
    app.run(debug=True)
