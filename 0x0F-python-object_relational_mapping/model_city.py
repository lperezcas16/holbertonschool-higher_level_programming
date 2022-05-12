#!/usr/bin/python3
""" Contains the City class and an instance call Base
"""


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


""" the base class is to create the tables class """
Base = declarative_base()


class City(Base):
    """class for the table states

    Args:
        Base (class): declarative base
    """
    __tablename__ = "cities"
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )
