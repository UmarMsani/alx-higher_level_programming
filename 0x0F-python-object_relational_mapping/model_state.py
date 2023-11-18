#!/usr/bin/python3
"""
Module: state_class_definition

This module contains the class definition of State and
an instance Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents the State class linked to the MySQL table states.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Replace'username','password','db_name' withur MySQL credentials & db name
    engine = create_engine('mysql+mysqldb:\
            //username:password@localhost:3306/db_name')

    # Create the tables defined by the classes inheriting from Base
    Base.metadata.create_all(engine)
