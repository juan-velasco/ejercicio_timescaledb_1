import psycopg2

CONNECTION = "postgres://user:password@timescaledb:5432/db"

conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()

sensors = [('a', 'floor'), ('a', 'ceiling'), ('b', 'floor'), ('b', 'ceiling')]
cursor = conn.cursor()
for sensor in sensors:
  try:
    # Insertar datos en la tabla relacional de sensores
    cursor.execute("INSERT INTO sensors (type, location) VALUES (%s, %s);",
                (sensor[0], sensor[1]))
  except (Exception, psycopg2.Error) as error:
    print(error.pgerror)

conn.commit()
cursor.close()