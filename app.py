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

app = Flask(__name__)

# 9.5.2
# Create the Welcome Route

# We can define the welcome route using the code below:

@app.route("/")

# First, create a function welcome() with a return statement. Add this line to your code:

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!\n
    Available Routes:\n
    /api/v1.0/precipitation\n
    /api/v1.0/stations\n
    /api/v1.0/tobs\n
    /api/v1.0/temp/start/end\n
    ''')

# 9.5.3
# Precipitation Route

@app.route("/api/v1.0/precipitation")
# Next, we will create the precipitation() function.

def precipitation():
    # Now we can add code to the function. This code may look almost identical to code you've written previously, 
    # but now we'll dive deeper into our precipitation analysis and figure out how to best integrate it into our application.
    # First, we want to add the line of code that calculates the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Next, write a query to get the date and precipitation for the previous year. Add this query to your existing code.
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()

    # Finally, we'll create a dictionary with the date as the key and the precipitation as the value. 
    # To do this, we will "jsonify" our dictionary. Jsonify() is a function that converts the dictionary to a JSON file.
    precip = {date: prcp for date, prcp in precipitation}
    
    return jsonify(precip)


# 9.5.4
# Stations Route

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()

    # We want to start by unraveling our results into a one-dimensional array. 
    # To do this, we want to use the function np.ravel(), with results as our parameter.
    # Next, we will convert our unraveled results into a list. 
    # To convert the results to a list, we will need to use the list function, which is list(), 
    # and then convert that array into a list. Then we'll jsonify the list and return it as JSON. 
    # Let's add that functionality to our code:
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


# 9.5.5
# Monthly Temperature Route

@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
    
# 9.5.6
# Statistics Route

# Just one more route to create! Our last route will be to report on the minimum, average, and maximum temperatures. 
# However, this route is different from the previous ones in that we will have to provide both a starting and ending date. 
# Add the following code to create the routes:

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# We need to add parameters to our stats()function: a start parameter and an end parameter. For now, set them both to None.
def stats(start=None, end=None):
    # With the function declared, we can now create a query to select the minimum, average, and maximum temperatures from our SQLite database. 
    # We'll start by just creating a list called sel, with the following code:
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # Since we need to determine the starting and ending date, add an if-not statement to our code. 
    # This will help us accomplish a few things. We'll need to query our database using the list that we just made. 
    # Then, we'll unravel the results into a one-dimensional array and convert them to a list. 
    # Finally, we will jsonify our results and return them.
        # In the following code, take note of the asterisk in the query next to the sel list. 
        # Here the asterisk is used to indicate there will be multiple results for our query: minimum, average, and maximum temperatures.
    if not end:
        results = session.query(*sel).filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    # Now we need to calculate the temperature minimum, average, and maximum with the start and end dates. 
    # We'll use the sel list, which is simply the data points we need to collect. 
    # Let's create our next query, which will get our statistics data.
    results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
    
# entering any date in the dataset as a start and end date. 
# The code will output the minimum, maximum, and average temperatures. 
# For example, let's say we want to find the minimum, maximum, and average temperatures for June 2017. 
# You would add the following path to the address in your web browser:
# /api/v1.0/temp/2017-06-01/2017-06-30





