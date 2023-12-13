# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
import datetime as dt
import numpy as np

from flask import Flask, jsonify

# Create engine
engine = create_engine("sqlite:///C:/Users/Aline/OneDrive/Desktop/Boot Camp/Week 10 Adv SQL/Resources/hawaii.sqlite")

#################################################
# Database Setup
#################################################
# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
# Create App
app = Flask(__name__)

#Define homepage to list all available routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

#################################################
# Flask Routes
#################################################

# Define most recent date in Measurement data set
# Calculate one year from most recent date
latest_date = dt.date(2017, 8 ,23)
a_year_ago = latest_date - dt.timedelta(days=365)

# Define routes for precipitation, stations, tobs, start date, and start/end date
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create session
    session = Session(engine)

    # Query precipitation data from last 12 months from the most recent date
    date_prcp = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date.between(a_year_ago, latest_date)).all()
    
    # Close session 
    session.close()

    # Make list
    date_precipitation = {date: prcp for date, prcp in date_prcp}

    # Return a list of jsonified precipitation data
    return jsonify(date_precipitation)

@app.route("/api/v1.0/stations")
def stations():
    # Create session
    session = Session(engine)

    # Query station data from the Station dataset
    all_stations = session.query(Station.station).all()

    # Close session 
    session.close()

    # Convert list of tuples into normal list
    stations = list(np.ravel(all_stations))

    # Return a list of jsonified station data
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create session
    session = Session(engine)

    # Query tobs data from last 12 months from the most recent date
    date_tobs = session.query(Measurement.tobs).\
    filter(Measurement.station == "USC00519281").\
    filter(Measurement.date.between(a_year_ago, latest_date)).all()

    # Close session
    session.close()

    # Convert list of tuples into normal list
    datetobs = list(np.ravel(date_tobs))

    # Return a list of jsonified tobs data
    return jsonify(datetobs)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def cal_temp(start=None, end=None):
    session = Session(engine)

    # Make a list to query min, avg, and max
    mam=[func.min(Measurement.tobs),
         func.avg(Measurement.tobs),
         func.max(Measurement.tobs)]
    
    # Check if there is an end date then do the task accordingly
    if end == None: 
        # Query the data from start date to the most recent date
        start_data = session.query(*mam).\
                            filter(Measurement.date >= start).all()
        # Convert list of tuples into normal list
        start_list = list(np.ravel(start_data))
        return jsonify(start_list)
    else:
        # Query the data from start date to the end date
        start_end_data = session.query(*mam).\
                            filter(Measurement.date >= start).\
                            filter(Measurement.date <= end).all()
        # Convert list of tuples into normal list
        start_end_list = list(np.ravel(start_end_data))
        return jsonify(start_end_list)

    # Close the session                   
    session.close()

#Define main branch
if __name__ == "__main__":
    app.run(debug=True)