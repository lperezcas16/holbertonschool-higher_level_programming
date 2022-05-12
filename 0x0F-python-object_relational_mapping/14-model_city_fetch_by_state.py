#!/usr/bin/python3
""" prints all City objects from the database hbtn_0e_14_usa
    format to display <state name>: (<city id>) <city name>
    Using the module SQLAlchemy
"""


import sqlalchemy
from sqlalchemy import create_engine, select, asc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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

    s = select([State.name, City.id, City.name]).where(
        City.state_id == State.id
    ).order_by(asc(City.id))

    rs = engine.execute(s)

    rows = rs.fetchall()
    for i in rows:
        print("{}: ({}) {}".format(i[0], i[1], i[2]))
