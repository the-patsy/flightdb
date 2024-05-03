import psycopg2 

# Establish connection to DB
conn = psycopg2.connect(database='postgres', user='patsy', password='password', host='127.0.0.1', port='5432'
)
conn.autocommit = True

# Create cursor object
cursor = conn.cursor()

# Test create
sql = '''CREATE database flight_database''';
cursor.execute(sql)
conn.close()
