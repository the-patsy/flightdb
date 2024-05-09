import psycopg2 

# Establish connection to DB
conn = psycopg2.connect(database='postgres', user='patsy', password='password', host='127.0.0.1', port='5432'
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
        arrivalAirportCandidatesCount INTEGER,
        callsign VARCHAR,
        departureAirportCandidatesCount INTEGER,
        estArrivalAirport VARCHAR,
        estArrivalAirportHorizDistance VARCHAR,
        estArrivalAirportVertDistance VARCHAR,
        estDepartureAirport VARCHAR,
        estDepartureAirportHorizDistance VARCHAR,
        estDepartureAirportVertDistance VARCHAR,
        firstSeen INTEGER,
        icao24  VARCHAR PRIMARY KEY,
        lastSeen INTEGER)
        """)
cursor.execute(commands)
conn.close()
