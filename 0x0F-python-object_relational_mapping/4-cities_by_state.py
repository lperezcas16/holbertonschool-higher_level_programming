#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    argv = sys.argv

    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    query_str = "SELECT cities.id, cities.name, states.name "
    query_str = query_str + "FROM cities, states "
    query_str = query_str + "WHERE state_id=states.id ORDER BY cities.id ASC;"

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
    cur.execute(query_str)

    """ tuple wiat all rows """
    rows = cur.fetchall()

    for row in rows:
        print(row)
