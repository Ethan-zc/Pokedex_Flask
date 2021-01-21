# Pokedex

#### 1. Project Type: A

#### 2. Group Members Name: Zichen Yang, Isaac Skorseth

#### 3. Link to Live Application: 

​			https://pokedex-finalproject.herokuapp.com/index

#### 4. Link to Github:

​			https://github.umn.edu/SKORS004/Pokedex

#### 5. List of Technologies/API Used:

​			PokeAPI: https://pokeapi.co/

#### 6. Detailed Description

​	The purpose of our project was to provide a centralized database for general pokemon information for fans of the games. Our website requires a user to make an account first before it is stored in our database with an encrypted password. From that point on, the user will have unlimited access to login and utilize the resource. We provide several tiers of functionality. Firstly, we provide a “gym leader” table. This “gym leader” table provides the following: name, region, location, type, badge, leader image, and badge image. This table encompasses all the gym leaders found in all the games. Within this table, if you click on the name of any given gym leader, it will pull up a table of their pokemon. This is our “many to many” relationship in the project; it connects the “gym leader” table and the “pokemon” table. Next, there’s a “cities” table. This table returns the following information: name, gym leader, region, connection location, and image. This table can be used in conjunction with the gym leader table to identify which gym leaders reside in which cities. It also is useful to identify different passages between cities, described as route numbers in the games. Finally, we have a table that simply encompasses a large list of pokemon. This table returns the following information: name, image, type, description, unique move, and location. Returning to the “gym leader” table, if you click on a gym leader’s name, it will query this table for his pokemon. You can search specific pokemon or filter by type to return only the pokemon you’re interested in. However, this list isn’t exhaustive, so we provided a means to search any other pokemon that aren’t currently stored in our database. To do this, we utilized the PokeAPI. Now, any pokemon can be returned to the user. The information the API provides is the following: name, image, special move, and a description as found in the games. After you’ve gotten your fill of pokemon, simply logout. You can return whenever you please to learn more about pokemon by simply logging in with the username and password you created when you first signed up. 

####   7. List of Controller and their short description

##### 	1. Pokedex_Index.py: 

​			This controller renders the index page of our web application. It is a blueprint from app.py. When 			/index page is required, it would return the rendering of view index.html.



##### 	2. PokemonApi.py:

​			This controller takes charge of communicating with PokeAPI.co. It is also a blueprint from app.py. 



##### 	3. app.py:

​			This is the most important controller in this project. It is the source of blueprint for all other 				                       			controllers. User management session, and database query session including gym leader 				         			information, their corresponding pokemons, pokemon table query, cities table query are all done in       			this controller. 



#### 8. List of Views and their short description
​		Note: All templates inherit from "bootstrap/base.html"
##### 	1. index.html:

​			This is the index page of the web application.

##### 	2. login.html:

​			This controls the front end communication between the user and our database. A successful login must be made before the user can have access to the other layers of our webservice. 

##### 	3. Signup.html:

​			This controls the addition of users to our database system. The user must input a valid username and password before it is stored in our "users" database with an encrypted password hashed from what was entered. 

##### 	4. Dashboard.html:

​			This is the dashboard page after user has logged in. This view file is in charge of four hyperlink that 			links to certain function of our application. It create hyperlink and use image as the context. The 			corresponding .css file is dashboard.css.

##### 	5. gymleader.html:

​			This controls the page of gym leader information function. It takes the input of gymleader list from 			app.py and render them as a table. It also has a filter function which would send 'POST' message to 			app.py to find certain gym leaders. 

##### 	6. Pokemon_filter.html:

​			This is the page for query certain pokemon from database. Similar to gymleader.html, it would take 			input pokemonlist from app.py and render them as a table. Filter funtion send ’POST‘ to query with 			condition. 

##### 	7. single_gymleader.html:

​			it draw the page for every single gym leader in our database. It would firstly take gymleader 				             			information from table gymleader, and then take pokemonlist of the certain gymleader from app.py. 

##### 	8. Addpokemon.html:

​			It is the view for api function. Since we cannot get all pokemons into our database, this view is built 			for searching more pokemons through api. The information got from api would be rendered as a 			table. 

##### 	9. Cities.html:	

​			it is bulit for the cities function. It takes input cities list from app.py and render them as a table. It 			would also send 'POST' request to query with condition. 

##### 	10. home.html:

​     Upon successful login, this provides an interface between the user and our database. Four options are available: gym leaders, cities, pokemon, and search pokemon. 

#### 9. List of Tables, their structure and short description			


#### User Table: id# | username | password(encrypted)

Every user has a unique id#. This is simply an integer that marks signup order of our webservice. The username is straighforward. The password is encrypted using 'sha256'. 

#### Pokemons Table: name(many-to-many) | description | unique move | location | type | image

All fields are self explanatory. The image column returns a url to an image which is then rendered in the template. The name is the query field necessary for our "many to many" relationship in this project. We compare the "name" from the "gym leaders" table and the "name" from the "pokemons" table and return a successful match. 

#### Cities Table: name | gym leader | region | connection locations | image

Again, the column are rather self explantory. Regions identify the encompassing location of the city (like saying "Minneapolis is in Minnesota"). The gym leader column provides a "one to one" relationship with our gym leader table. The image column returns the url of an image rendered in the template html. 

#### Gym Leader Table: name | location | type | badge | region | leader image | badge image

Location and city provide "one to one" relationships with the "cities" table. Clicking on the name of gym leader in this table returns a list of pokemon they possess. This is a "many to many" relationship between this table and our "pokemons" table. Two image url's are returned and rendered in the template html respectively. 

#### Gym Leaders - Pokemons Table: gymleader name | pokemon name

This is our intermediate table for the "many to many" relationship. It stores an instance of "gymleader name" and "pokemon name" for every pokemon a gym leader owns. When a gym leader is called from the "gym leader" table, it first filters the list by "gymleader name = name", and then query's the "pokemons" table for each "pokemon name" instance found in the "Gym leaders - Pokemons" table.   

#### 10. References:

https://pokeapi.co/

https://pythonhosted.org/Flask-Bootstrap/

https://www.youtube.com/watch?v=8aTnmsDMldY

<img src="/static/database_structure.jpg">

