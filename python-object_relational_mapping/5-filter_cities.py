#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
"""

import sys
import MySQLdb

if __name__ == "__main__":

    dbase = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )


    cursor = dbase.cursor()
    SQL = "SELECT cities.name FROM cities"
    JOIN = "INNER JOIN states ON cities.state_id = states.id"
    WHERE = "WHERE states.name = '{}'".format(sys.argv[4])
    SQL_query = "{} {} {};".format(SQL, JOIN, WHERE)
    cursor.execute(SQL_query)
    results=cursor.fetchall()
    print(", ".join([state[0] for state in results]))
