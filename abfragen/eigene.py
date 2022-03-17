import os
import sqlite3
from pprint import pprint

DATABASE_FILE = "database.db"

def main():
    if not os.path.isfile(DATABASE_FILE):
        print("Datenbank nicht gefunden")
        return

    con = sqlite3.connect(DATABASE_FILE)

    query = open("abfragen/eigene.sql", "r").read()
    cur = con.cursor()
    cur.execute(query)

    pprint(cur.fetchall())

    con.close()

if __name__ == "__main__":
    main()