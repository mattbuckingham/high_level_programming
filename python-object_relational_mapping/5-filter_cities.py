#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    takes in the name of a state as an argument and lists all cities
    """

    dbase = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    state = sys.argv[4]

    cursor = dbase.cursor()
    SQL = "SELECT cities.name FROM cities INNER JOIN states ON cities.state_id =
states.id WHERE states.name = '{}'".format(state)
    cursor.execute(SQL)
    rows=cursor.fetchall()
    results=[]
    for row in rows:
        for col in row:
            results.append(col)
    print(','.join(results))
