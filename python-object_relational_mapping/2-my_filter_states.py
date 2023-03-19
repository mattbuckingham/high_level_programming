#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    dbase = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    state = sys.argv[4]
    cursor = dbase.cursor()
    cursor.execute(
"SELECT * FROM states WHERE BINARY name LIKE {} ORDER BY id ASC".format(state))
    results = cursor.fetchall()

    for row in results:
        print(row)
