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

pokemon_api = Blueprint('pokemon_api', __name__)

@pokemon_api.route("/get", methods=['GET', 'POST'])
def get():
    if request.method == 'POST':
        pokemon = request.form['Pokemon_Name']
        pokemon = pokempn.lower()
        # pokemon = request.args.get('name')
        url = "http://pokeapi.co/api/v2/pokemon/"
        apiURL = url + pokemon
        response = requests.get(apiURL)
        data = response.json()
        moves = data["moves"]
        moves = moves[0]
        moves = moves["move"]
        moves = moves["name"]
        species = data["species"]
        speciesURL = species["url"]
        speciesURL = requests.get(speciesURL)
        speciesURL = speciesURL.json()
        speciesURL = speciesURL["flavor_text_entries"]
        species = species["name"]
        picture = data["sprites"]
        picture = picture["front_default"]
        gameNames = ["moon", "alpha-sapphire","blue","gold", "silver", 
                    "crystal", "firered", "emerald", "heartgold", "x", "sun"]
        description = ""
        for i in speciesURL:
            if(i["language"]["name"] == "en"):
                if(i["version"]["name"] in gameNames):
                    description = description + " " + i["flavor_text"].encode("ascii", "ignore").decode("ascii")
        return render_template('home.html', picture = picture, moves = moves, species = species, Description = description)
    elif request.method == 'GET':
        return render_template('home.html')
    # result_list = [pokemon,picture,moves,species,description]

    
    # db.sessione.execute('insert into pokemons(name, description, uniquemove, image) values( :cname, :cdescription, :cunique_move, :cimage)', {'cname': pokemon, 'cdescription': description, 'cunique_move': moves, 'cimage': image})



    # Here all the info of certain Pokemon is got. 




