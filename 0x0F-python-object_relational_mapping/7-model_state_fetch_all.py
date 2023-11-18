#!/usr/bin/python3
"""
Module: list_states

This module lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password db_name".format(sys.argv[0]))
    else:
        username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

        # Create an engine to establish a connection to the MySQL database
        engine = create_engine('mysql+mysqldb://{}:{}\
                @localhost:3306/{}'.format(username, password, db_name))

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Query all State objects and sort them by states.id in ascending order
        states = session.query(State).order_by(State.id).all()

        # Display results as per requirement
        for state in states:
            print("{}: {}".format(state.id, state.name))

        # Close the session
        session.close()
