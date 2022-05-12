#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa
    Using the module SQLAlchemy
"""


import sqlalchemy
from sqlalchemy import create_engine, select, asc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    """ create_engine function not conects with the database """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username,
            password,
            database_name
        ),
        pool_pre_ping=True
    )
    """ to connect with the db but functions without engine.connect() """
    """ engine.connect() """

    s = select([State]).order_by(asc(State.id))

    rs = engine.execute(s)
    for row in rs:
        contr = 0
        for i in row:
            if contr:
                print(end=": ")
            contr = 1
            print(i, end="")
        print()
