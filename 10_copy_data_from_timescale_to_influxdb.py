import psycopg2
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

CONNECTION = "postgres://user:password@timescaledb:5432/db"
TOKEN = 'MpCpEGm1092T3PrbaUFGIRtadf1ggNMQx-IX55f_hLIYFG6E9JF9M3NdbnMlkpkT080YRkHgBoyWtIPAj_MJrQ==' # cambiar por el token de influxdb
ORG = 'org1'
BUCKET = 'bucket1'
URL = 'http://influxdb:8086'

conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()

query = """
        SELECT time, sensor_id, temperature, cpu, type, location
        FROM sensor_data
        JOIN sensors ON sensors.id = sensor_data.sensor_id
        ORDER BY time DESC;
        """

cursor.execute(query)



# Crear cliente de InfluxDB
client = InfluxDBClient(url=URL, token=TOKEN, org=ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

for row in cursor.fetchall():
    point = Point("sensor_data") \
        .tag("type", row[4]) \
        .tag("location", row[5]) \
        .field("temperature", row[2]) \
        .field("cpu", row[3]) \
        .time(row[0], WritePrecision.NS)
    write_api.write(bucket=BUCKET, org=ORG, record=point)    

cursor.close()