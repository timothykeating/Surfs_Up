import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite")

# The create_engine() function allows us to access and query our SQLite database file. Now let's reflect the database into our classes.

Base = automap_base()

# Add the following code to reflect the database:

Base.prepare(engine, reflect=True)

# With the database reflected, we can save our references to each table. 
# Again, they'll be the same references as the ones we wrote earlier in this module.
#  We'll create a variable for each of the classes so that we can reference them later, as shown below.

Measurement = Base.classes.measurement
Station = Base.classes.station

# Finally, create a session link from Python to our database with the following code:

session = Session(engine)

# Set Up Flask
# To define our Flask app, add the following line of code. This will create a Flask application called "app."

app2 = Flask(__name__)

# 9.5.2
# Create the Welcome Route

# We can define the welcome route using the code below:

@app2.route("/")

# First, create a function welcome() with a return statement. Add this line to your code:

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

