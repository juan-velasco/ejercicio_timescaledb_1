import psycopg2
from pgcopy import CopyManager

CONNECTION = "postgres://user:password@timescaledb:5432/db"

conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()

# Agrupar los datos de los sensores por ubicación y tipo, en intervalos de 5 minutos
query = """
           SELECT time_bucket('5 minutes', time) AS five_min, avg(cpu)
           FROM sensor_data
           JOIN sensors ON sensors.id = sensor_data.sensor_id
           WHERE sensors.location = %s AND sensors.type = %s
           GROUP BY five_min
           ORDER BY five_min DESC;
           """

location = "floor"
sensor_type = "a"
data = (location, sensor_type)
cursor.execute(query, data)
results = cursor.fetchall()

# Recorrer results mostrando línea a línea
for row in results:
    print(row)

cursor.close()