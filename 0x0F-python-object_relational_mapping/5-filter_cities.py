#!/usr/bin/python3
""" takes in the name of a state as an argument and lists all cities of that
    state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    argv = sys.argv

    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    user_input = argv[4]

    valid = 1

    chars_invalid = (";", "'", "-", "/*", "*/", "xp_")

    for i in chars_invalid:
        if i in user_input:
            valid = 0

    if valid:
        user_input = "'{}'".format(user_input)
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
        query_str = "SELECT cities.name FROM cities, states "
        query_str = query_str + "WHERE state_id=states.id AND states.name = "

        query_str1 = " ORDER BY cities.id;"

        cur.execute(query_str + user_input + query_str1)

        """ tuple wiat all rows """
        rows = cur.fetchall()

        contr = 0
        for row in rows:
            if contr:
                print(end=", ")
            for i in row:
                print(i, end="")
                contr = 1
        print()
