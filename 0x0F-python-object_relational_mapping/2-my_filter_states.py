#!/usr/bin/python3
""" takes in an argument and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    argv = sys.argv

    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    user_input = argv[4]

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
    query_str = "SELECT * FROM states WHERE name LIKE BINARY "
    cur.execute(query_str + "'{}' ORDER BY id ASC".format(user_input))

    """ tuple wiat all rows """
    rows = cur.fetchall()

    for row in rows:
        print(row)
