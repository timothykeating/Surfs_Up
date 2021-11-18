from flask import Flask

app = Flask(__name__)

# First, we need to define the starting point, also known as the root. To do this, we'll use the function @app.route('/').
@app.route('/')

# Next, create a function called hello_world(). Whenever you make a route in Flask, 
# you put the code you want in that specific route below @app.route(). Here's what it will look like:
@app.route('/')
def hello_world():
    return 'Hello world'

# Run a Flask App
# The process of running a Flask app is a bit different from how we've run Python files. 
# To run the app, we're first going to need to use the command line to navigate to the folder where we've saved our code.
# Start by opening up Anaconda Powershell. Once you've done that, enter this command -->
# set FLASK_APP=app.py

# Now let's run our Flask app. To do this, type the following command in your command line and press Enter:
#  flask run

# When you run this command, you'll notice a line that says "Running on" followed by an address. This should be your localhost address and a port number.
# Copy and paste your localhost address into your web browser. 

# SKILL DRILL
# Think of some simple code from which you could create a route. Then try to create a new route implementing that logic.
@app.route('/')
def timmmmmah():
    return 'Timmmmmah!!!!!!'

    # this did not do anything, alls i'm getting is "hello world" on the website

# 9.5.1
# Set Up the Database and Flask
#  ... go to app2.py file





