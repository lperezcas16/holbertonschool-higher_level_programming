#!/usr/bin/python3
""" changes the name of a State object from the database hbtn_0e_6_usa
    Using the module SQLAlchemy
"""


import sqlalchemy
from sqlalchemy import create_engine, select, insert, update
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

    s = update(State).where(
        State.id == 2
    ).values(
        name="New Mexico"
    )

    rs = engine.execute(s)
