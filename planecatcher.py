import datetime
import time
from opensky_api import OpenSkyApi
import psycopg2

# Convert input into UNIX timestamp
def convert_dmy_to_unix(d, m, y):
    date_time = datetime.datetime(int(y), int(m), int(d), 0, 0)
    return (time.mktime(date_time.timetuple()))

# TODO Add to function a way to parse the flight data into postgres
""" Function for adding values to postgres DB.
def add_db_data():
    # Establish connection to DB
    conn = psycopg2.connect(
            database='postgres',
            user='patsy',
            password='password',
            host='127.0.0.1',
            port='5432'
    )

    conn.autocommit = True

    # Create cursor object
    cursor = conn.cursor()

    print(cursor.fetchone())

    conn.close()
"""

# Gather timeframe for DB entry

""" Temporarily not taking input code for hardcoded test case.
input_start_year = input('Enter start date year (YYYY): ')
input_start_month = input('Enter start date month (1-12): ')
input_start_day = input('Enter start date day (1-31): ')
input_start_time = input('Enter start date time (hh:mm:ss): ')
input_end_time = input('Enter end time (hh:mm:ss): ')
start_time_split = input_start_time.split(':')
end_time_split = input_end_time.split(:)
# Covert to unix timestamp and add time in seconds to have variables for data pull.
startdate = 
"""

# Test data to delete
input_start_year = 2024
input_start_month = 1
input_start_day = 1
input_end_year = 2024
input_end_month = 1
input_end_day = 2

# Hardcoded starttimes
startdate = 1517227200
enddate = 1517230800

# Test API

api = OpenSkyApi()
data = api.get_flights_from_interval(startdate, enddate)
for flight in data:
    print(flight)

#create_db()
