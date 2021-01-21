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
from Pokedex_index import pokedex_index
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Pokedex_test.db'
app.config['SECRET_KEY'] = 'supersecret'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

app.register_blueprint(pokemon_api)
app.register_blueprint(pokemon_api, url_prefix='/pokemon')

app.register_blueprint(pokedex_index)
app.register_blueprint(pokedex_index, url_prefix='/index')

# from DatabaseQuery import database_controller

# app.register_blueprint(database_controller)
# app.register_blueprint(database_controller, url_prefix='/database')

login = LoginManager(app)
login.login_view = 'login'


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique = True)
    password = db.Column(db.String(80))

@login.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max = 80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max = 15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max = 80)])

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard')+"?username="+user.username)
        flash('Invalid Username or Password')
    return render_template('login.html', form = form)

@app.route('/signup', methods = ["GET", "POST"])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method = 'sha256')
        new_user = Users(username = form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form = form)

@app.route('/dashboard')
@login_required
def dashboard():
    # username = request.args.get('username')
    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/cities', methods=["GET", "POST"])
@login_required
def cities():
    if request.method == "POST":
        city_region = request.form["City_Region"]
        city_region = city_region.capitalize()
        
        if (city_region == '') :
            res = db.session.execute('select * from cities')
        elif (city_region != ''):
            res = db.session.execute('select * from cities where region = :select_region', {'select_region': city_region})

    elif request.method=="GET":
        res = db.session.execute('select * from cities')

    city_list = res.fetchall()

    return render_template('cities.html', cities=city_list)


@app.route('/gymleaders', methods=["GET", "POST"])
@login_required
def gymleaders():
    if request.method=="POST":
        leader_type = request.form['Leader_Type']
        leader_region = request.form['Leader_Region']
        leader_type = leader_type.capitalize()
        leader_region = leader_region.capitalize()

        if (leader_type == "" and leader_region != ""):
            res = db.session.execute('select * from gymleader where region = :select_region', {'select_region': leader_region})
        elif (leader_type != "" and leader_region == ""):
            res = db.session.execute('select * from gymleader where type = :select_type', {'select_type': leader_type})
        elif (leader_type != "" and leader_region != ""):
            res = db.session.execute('select * from gymleader where type = :select_type and region = :select_region', {'select_type': leader_type, 'select_region':leader_region})
        elif (leader_type == "" and leader_region == ""):
            res = db.session.execute('select * from gymleader')

    elif request.method=="GET":
        res = db.session.execute('select * from gymleader')
        
    gymleaders_list = res.fetchall()
    return render_template('gymleader.html', gymleaders=gymleaders_list)



@app.route('/single_gymleader/<name>')
@login_required
def leader_pokemon_list(name):
    leader_name = name;
    leader_name = leader_name.capitalize()
    res = db.session.execute('select * from gymleader where name= :cname', {'cname': leader_name})
    gymleader = res.fetchall()
    res = db.session.execute('select pokemons.* from pokemons left join gymleaders_pokemons on pokemons.name=gymleaders_pokemons.pokemon_name left join gymleader on gymleaders_pokemons.gymleader_name=gymleader.name where gymleaders_pokemons.gymleader_name= :select_name', {'select_name': leader_name})
    gymleader_poke_list = res.fetchall()

    return render_template('single_gymleader.html', poke_list=gymleader_poke_list, gymleaders=gymleader, name=leader_name)

@app.route('/pokemondatabase', methods=['GET', 'POST'])
@login_required
def pokemondatabase():
    if request.method == 'POST':
        pokemon_name = request.form['Pokemon_Name']
        pokemon_name = pokemon_name.capitalize()
        pokemon_type = request.form['Pokemon_Type']
        pokemon_type = pokemon_type.capitalize()

        if (pokemon_name != '' and pokemon_type == ''):
            res = db.session.execute('select * from pokemons where name= :cname', {'cname': pokemon_name})
        elif (pokemon_name == '' and pokemon_type != ''):
            res = db.session.execute('select * from pokemons where type= :ctype', {'ctype': pokemon_type})
        elif (pokemon_name != '' and pokemon_type != ''):
            res = db.session.execute('select * from pokemons where name= :cname and type= :ctype', {'cname': pokemon_name, 'ctype': pokemon_type})
        elif (pokemon_name == '' and pokemon_type == ''):
            res = db.session.execute('select * from pokemons')

    elif request.method == 'GET':

        res = db.session.execute('select * from pokemons')

    pokemon_list = res.fetchall()
    return render_template('pokemon_filter.html', pokemon_list=pokemon_list)




if __name__=="__main__":
    app.run(debug=True)
