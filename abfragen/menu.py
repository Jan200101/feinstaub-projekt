import os
import sqlite3
from pprint import pprint
from typing import List
import datetime

DATABASE_FILE = "database.db"

TEMPERATUR = "Temperatur"
LUFTFEUCHTIGKEIT = "Luftfeuchtigkeit"
FEINSTAUB = "Feinstaub"

BASE_QUERY = """
SELECT
    MIN({wert}) as "Maximal {type}",
    MAX({wert}) as "Minimal {type}",
    AVG({wert}) as "Durschnitts {type}"
FROM {table}
WHERE
    strftime('%d.%m.%Y', datetime) = "{datestr}"
"""

def choice(options: List[str], prompt=None, *,
           case_insensitive=False, error_msg=None,
           display_options=False) -> str:

    if not isinstance(prompt, str):
        prompt = ""

    if display_options:
        prompt += "[" + ", ".join(options) + "]"

    if case_insensitive:
        options = [x.lower() for x in options]


    while True:
        inp = input(prompt)
        inp_cmp = inp
        if case_insensitive:
            inp_cmp = inp_cmp.lower()
        if inp_cmp in options:
            return inp
        elif error_msg:
            print(error_msg)

    return ""

def date_input() -> datetime.date:

    while True:
        inp = input()

        try:
            day, month, year = map(int, inp.split('.'))
            if year < 2000: continue

            return datetime.date(year, month, day)
        except ValueError:
            pass


def main() -> None:
    if not os.path.isfile(DATABASE_FILE):
        print("Datenbank nicht gefunden")
        return


    print("Wertetyp")
    sel = choice([
            TEMPERATUR,
            LUFTFEUCHTIGKEIT,
            FEINSTAUB
        ],
        case_insensitive=True,
        display_options=True
    )

    print("Datum")
    date = date_input()
    date_str = date.strftime("%d.%m.%Y")

    con = sqlite3.connect(DATABASE_FILE)

    query = None
    if sel == TEMPERATUR:
        query = BASE_QUERY.format(type=sel, wert="tempwert", table="temperaturUndLuftdruck", datestr=date_str)
    elif sel == LUFTFEUCHTIGKEIT:
        query = BASE_QUERY.format(type=sel, wert="luftwert", table="temperaturUndLuftdruck", datestr=date_str)
    elif sel == FEINSTAUB:
        query = BASE_QUERY.format(type=sel, wert="p1wert", table="feinstaubsensor", datestr=date_str)

    if query:
        cur = con.cursor()
        cur.execute(query)
        data = cur.fetchall()[0]

        print(
        """
        Maximal {type}: {max}\n
        Minimal {type}: {min}\n
        Durchscnitts {type}: {avg}\n
        """.format(type=sel, max=data[0], min=data[1], avg=data[2]))

    con.close()

if __name__ == "__main__":
    main()