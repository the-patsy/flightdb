import datetime
import time
from opensky_api import OpenSkyApi
import psycopg2

# Convert input into UNIX timestamp
def convert_dmy_to_unix(d, m, y):
    date_time = datetime.datetime(int(y), int(m), int(d), 0, 0)
    return (time.mktime(date_time.timetuple()))

#def add_db_data():


# Establish connection to DB
conn = psycopg2.connect(database='postgres', user='patsy', password='password', host='127.0.0.1', port='5432'
)
conn.autocommit = True

# Create cursor object
cursor = conn.cursor()

# Test create
sql = '''CREATE database Flight_database''';
cursor.execute(sql)
conn.close()
# Create api variable
api = OpenSkyApi()

# Gather timeframe for DB entry

""" TODO uncomment and remove hardcoded test data.
input_start_year = input('Enter start date year (YYYY): ')
input_start_month = input('Enter start date month (1-12): ')
input_start_day = input('Enter start date day (1-31): ')
input_end_year = input('Enter end date year (YYYY): ')
input_end_month = input('Enter end date month (1-12); ')
input_end_day = input('Enter end date day (1-31): ')
"""

# Test data to delete
input_start_year = 2024
input_start_month = 1
input_start_day = 1
input_end_year = 2024
input_end_month = 1
input_end_day = 2

# Get days as UNIX timestamps
startdate = convert_dmy_to_unix(input_start_day, input_start_month, input_start_year)
enddate = convert_dmy_to_unix(input_end_day, input_end_month, input_end_year)

#create_db()
