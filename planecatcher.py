import datetime
import time
from opensky_api import OpenSkyApi

# Create api variable
api = OpenSkyApi()

# Gather timeframe for DB entry

input_start_year = input('Enter start date year (YYYY): ')
input_start_month = input('Enter start date month (1-12): ')
input_start_day = input('Enter start date day (1-31): ')
input_end_year = input('Enter end date year (YYYY): ')
input_end_month = input('Enter end date month (1-12); ')
input_end_day = input('Enter end date day (1-31): ')

# Convert input into UNIX timestamp

start_date_time = datetime.datetime(int(input_start_year), int(input_start_month), int(input_start_day), 0, 0)

print("Date_time test -> ",start_date_time)
print("unix_timestamp -> ",(time.mktime(start_date_time.timetuple())))
