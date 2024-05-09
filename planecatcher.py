import datetime
import time
from opensky_api import OpenSkyApi
import psycopg2

# Convert input into UNIX timestamp
def convert_dmy_to_unix(d, m, y, h, minute):
    date_time = datetime.datetime(int(y), int(m), int(d), int(h), int(minute))
    return (time.mktime(date_time.timetuple()))

# TODO Add to function a way to parse the flight data into postgres

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

# Gather timeframe for DB entry

""" Temporarily not taking input code for hardcoded test case.
input_start_year = input('Enter start date year (YYYY): ')
input_start_month = input('Enter start date month (1-12): ')
input_start_day = input('Enter start date day (1-31): ')
input_start_time = input('Enter start date time (hh:mm): ')
input_end_time = input('Enter end time (hh:mm): ')
start_time_split = input_start_time.split(':')
end_time_split = input_end_time.split(:)

# Covert to unix timestamp and add time in seconds to have variables for data pull.
calc_start = convert_dmy_to_unix(input_start_year, input_start_month, input_start_day, start_time_split[0], start_time_split[1])
cal_end = calc_start + (60 * 60 * start_time_split[0]) + (60 * start_time_split[1])
startdate = int(calc_start)
enddate = int(calc_end)
"""

# Hardcoded times
startdate = 1517227200
enddate = 1517230800

# Test API

api = OpenSkyApi()
data = api.get_flights_from_interval(startdate, enddate)
"""
for flight in data:
    print(flight)
    confimline = input('NEXT')
"""
#add_db_data()
