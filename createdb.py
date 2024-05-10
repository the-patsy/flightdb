import psycopg2 

# Establish connection to DB
conn = psycopg2.connect(database='flight_database', user='patsy', password='password', host='127.0.0.1', port='5432'
)
conn.autocommit = True

# Create cursor object
cursor = conn.cursor()

# Test create
#sql = '''CREATE database flight_database''';
#cursor.execute(sql)

commands = (
    """
    CREATE TABLE flights (
        arrivalAirportCandidatesCount VARCHAR,
        callsign VARCHAR,
        departureAirportCandidatesCount VARCHAR,
        estArrivalAirport VARCHAR,
        estArrivalAirportHorizDistance VARCHAR,
        estArrivalAirportVertDistance VARCHAR,
        estDepartureAirport VARCHAR,
        estDepartureAirportHorizDistance VARCHAR,
        estDepartureAirportVertDistance VARCHAR,
        firstSeen VARCHAR,
        icao24  VARCHAR PRIMARY KEY,
        lastSeen VARCHAR)
        """)
cursor.execute(commands)
conn.close()
