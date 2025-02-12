import psycopg2
from pgcopy import CopyManager

CONNECTION = "postgres://user:password@timescaledb:5432/db"

conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()

# Agrupar los datos de los sensores por ubicación y tipo, en intervalos de 5 minutos
query = """
           SELECT five_min, avg FROM cpu_5_minutes
           WHERE location = %s AND type = %s
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