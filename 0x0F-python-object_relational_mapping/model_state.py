#!/usr/bin/python3
""" Contains the State class and an instance call Base
"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


""" the base class is to create the tables class """
Base = declarative_base()


class State(Base):
    """class for the table states

    Args:
        Base (class): declarative base
    """
    __tablename__ = "states"
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)
