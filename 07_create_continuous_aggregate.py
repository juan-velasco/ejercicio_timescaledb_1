import psycopg2
from pgcopy import CopyManager

CONNECTION = "postgres://user:password@timescaledb:5432/db"

conn = psycopg2.connect(CONNECTION)
conn.autocommit = True
cursor = conn.cursor()

# Agrupar los datos de los sensores por ubicación y tipo, en intervalos de 5 minutos
query = """
        CREATE MATERIALIZED VIEW cpu_5_minutes
        WITH (timescaledb.continuous) AS
        SELECT time_bucket('5 minutes', time) AS five_min, avg(cpu), sensors.location, sensors.type
        FROM sensor_data
        JOIN sensors ON sensors.id = sensor_data.sensor_id
        GROUP BY five_min, sensors.location, sensors.type;
        """

cursor.execute(query)

conn.autocommit = False
conn.commit()
cursor.close()