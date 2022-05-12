#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    argv = sys.argv

    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    """ connection to a db """
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database_name,
        port=3306
    )

    """ Nos da la capacidad de tener múltiples entornos de trabajo """
    cur = db.cursor()

    """ execute to execte a query """
    query_str = "SELECT * FROM states WHERE name LIKE BINARY 'N%'"
    cur.execute(query_str + " ORDER BY id ASC")

    """ tuple wiat all rows """
    rows = cur.fetchall()

    for row in rows:
        print(row)
