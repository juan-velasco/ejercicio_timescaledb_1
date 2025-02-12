import psycopg2

CONNECTION = "postgres://user:password@timescaledb:5432/db"

conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()

query_create_sensors_table = """CREATE TABLE sensors (
                                    id SERIAL PRIMARY KEY,
                                    type VARCHAR(50),
                                    location VARCHAR(50)
                                );
                                """

cursor = conn.cursor()
# see definition in Step 1
cursor.execute(query_create_sensors_table)
conn.commit()
cursor.close()