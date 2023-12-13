# sqlalchemy-challenge

## Challenge Instructions
Use Python and SQLAlchemy to achieve basic climate analysis and data exploration of the climate database in Hawaii, specifically with the use of SQLAlchemy ORM queries, Pandas, and Matplotlib. Based on the initial analysis, a Flask API was designed by using these queries.

## Climate Analysis and Exploration

Precipitation Analysis:
- A query was designed to retrieve the last 12 months of precipitation data
- The date and prcp values of the query results were selected and loaded into a Pandas DataFrame
- The results were sorted by date and plotted using plot method
- A summary statistics for the precipitation data was displayed using Pandas

Station Analysis:
- A query was designed to calculate the total number of stations in Hawaii
- The query finds the most active stations using functions as func.min, func.max, func.avg, and func.count
- Another query was designed to retrieve the last 12 months of temperature observation data (TOBS), which were later filtered by the station with the highest number of observations and plotted as a histogram with bins=12

## Climate App
Design App with Flask API based on the queries from above and Flask jsonify was used to convert API data into a valid JSON response object

- /
Start at the homepage.
List all the available routes.

- /api/v1.0/precipitation
Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary.

- /api/v1.0/stations
Return a JSON list of stations from the dataset.

- /api/v1.0/tobs
Query the dates and temperature observations of the most-active station for the previous year of data.
Return a JSON list of temperature observations for the previous year.

- /api/v1.0/<start> and /api/v1.0/<start>/<end>
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
