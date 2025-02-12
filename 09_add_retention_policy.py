import psycopg2

CONNECTION = "postgres://user:password@timescaledb:5432/db"

conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()

# crear retention policy
query = "SELECT add_retention_policy('sensor_data', INTERVAL '30 days');"

cursor.execute(query)

# commit changes to the database to make changes persistent
conn.commit()

cursor.close()