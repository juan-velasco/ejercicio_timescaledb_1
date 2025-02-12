import psycopg2

CONNECTION = "postgres://user:password@timescaledb:5432/db"

conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()

# create sensor data hypertable
query_create_sensordata_table = """CREATE TABLE sensor_data (
                                        time TIMESTAMPTZ NOT NULL,
                                        sensor_id INTEGER,
                                        temperature DOUBLE PRECISION,
                                        cpu DOUBLE PRECISION,
                                        FOREIGN KEY (sensor_id) REFERENCES sensors (id)
                                    );
                                    """

query_create_sensordata_hypertable = "SELECT create_hypertable('sensor_data', by_range('time'));"

cursor.execute(query_create_sensordata_table)
cursor.execute(query_create_sensordata_hypertable)

# commit changes to the database to make changes persistent
conn.commit()

cursor.close()