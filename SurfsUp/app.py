# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
        return 'Hello World'

@app.route(/api/v1.0/precipitation)
def precipitation():
    print("Server received request for 'Precipitation' page...")
    return "Welcome to my 'About' page!"

def justice_league():
    """Return the justice league data as json"""

    return jsonify(justice_league_members)


@app.route(/api/v1.0/stations)
def stations():
     
@app.route(/api/v1.0/tobs)
def tobs():
     
@app.route(/api/v1.0/<start>)
def starts():
     
@app.route(/api/v1.0/<start>/<end>)

@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)


def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/measurements<br/>"
        f"/api/v1.0/station<br/>"
    )

if __name__ == "__main__":
    app.run(debug=True)
