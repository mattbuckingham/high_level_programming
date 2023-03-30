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

    state_list = sys.argv[4]

    cursor = dbase.cursor()
    SQL = "SELECT cities.name FROM cities"
    JOIN = "INNER JOIN states ON cities.state_id = states.id"
    WHERE = "WHERE states.name = '{}'".format(state_list)
    SQL_query = "{} {} {};".format(SQL, JOIN, WHERE)
    cursor.execute(SQL_query, (state_list,))
    results=cursor.fetchall()
    print(','.join([state[1] for state in results]))
