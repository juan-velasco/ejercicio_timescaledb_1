import psycopg2
from pgcopy import CopyManager

CONNECTION = "postgres://user:password@timescaledb:5432/db"

conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()

query = "SELECT * FROM sensor_data;"
cursor.execute(query)
for row in cursor.fetchall():
    print(row)

cursor.close()