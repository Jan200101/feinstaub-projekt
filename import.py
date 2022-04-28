import os
import csv
import sqlite3

DATA_DIR="data"
DATABASE="database.db"

sensors = {
    "dht22": {
        "table": "temperaturUndLuftdruck",
        "mapping": {
            "sensor_id": "SensorID",
            "timestamp": "datetime",
            "humidity": "luftwert",
            "temperature": "tempwert"
        }
    },
    "sds011": {
        "table": "feinstaubsensor",
        "mapping": {    
            "sensor_id": "SensorID",
            "timestamp": "datetime",
            "P1": "p1wert",
            "P2": "p2wert"
        }
    }
}


def main():
    if not os.path.isdir(DATA_DIR):
        print("Daten wurden nicht heruntergeladen")
        return

    count = 0
    con = sqlite3.connect(DATABASE)

    for sensor, conf in sensors.items():
        table = conf["table"]
        mapping = conf["mapping"]
        mapping_count = len(mapping)

        with open("schema/{}.sql".format(table), "r") as schema:
            schema = schema.read()
            cur = con.cursor()
            try:
                cur.executescript(schema)
            except sqlite3.OperationalError:
                pass

        TABLE_PLACEHOLDERS = ", ".join(mapping.values())
        VALUE_PLACEHOLDER = ", ".join([":{}".format(key) for key in mapping.keys()])

        QUERY = """
INSERT 
INTO {0}({1})
VALUES ({2})    
""".format(table, TABLE_PLACEHOLDERS, VALUE_PLACEHOLDER)

        for root, dirs, files in os.walk("{}/{}".format(DATA_DIR, sensor)):
            for name in files:
                if not name.endswith(".csv"):
                    continue

                full_name = "{}/{}".format(root, name)
                
                with open(full_name, "r") as raw_data:
                    data = csv.DictReader(raw_data, delimiter=";")
                    data = list(data)

                    cur = con.cursor()
                    cur.executemany(QUERY, data)

    con.commit()
    con.close()

if __name__ == "__main__":
    main()