DATA_DIR="data"
DATABASE="database.db"
TABLE_NAME="table"

# import schemas
echo "Loading table schemas"
sqlite3 "${DATABASE}" < schema/feinstaub.sql
sqlite3 "${DATABASE}" < schema/temperaturluftdruck.sql
sqlite3 "${DATABASE}" < schema/import.sql

# import CSV into import tables
echo "Importing DHT22"
find . -type f -path "*/${DATA_DIR}/dht22/*.csv" | xargs -I% sqlite3 "${DATABASE}" \
".mode csv" \
".separator ;" \
".import --skip 1 % DHT22_SCHEMA" \
".exit"

echo "Migrating DHT22"
sqlite3 "${DATABASE}" \
"
INSERT OR IGNORE INTO temperaturUndLuftdruck(SensorID, datetime, luftwert, tempwert)
SELECT sensor_id, timestamp, humidity, temperatur
FROM DHT22_SCHEMA;
" \
"DROP TABLE DHT22_SCHEMA;"


echo "Importing SDS011"
find . -type f -path "*/${DATA_DIR}/sds011/*.csv" | xargs -I% sqlite3 "${DATABASE}" \
".mode csv" \
".separator ;" \
".import --skip 1 % SDS011_SCHEMA" \
".exit"

echo "Migrating SDS011"
sqlite3 "${DATABASE}" \
"
INSERT OR IGNORE INTO feinstaubsensor(SensorID, datetime, p1wert, p2wert)
SELECT sensor_id, timestamp, P1, P2
FROM SDS011_SCHEMA;
" \
"DROP TABLE SDS011_SCHEMA;"
