#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    lists all cities from the database hbtn_0e_4_usa
    """

    dbase = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    SQL = "SELECT cities.id, cities.name, states.name FROM cities"
    JOIN = "INNER JOIN states ON cities.state_id = states.id"

    data = db.cursor.execute('{} {}'.format(SQL, JOIN))
    for row in data:
        print(row)
