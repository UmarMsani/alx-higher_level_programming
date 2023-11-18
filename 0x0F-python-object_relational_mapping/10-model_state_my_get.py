#!/usr/bin/python3
"""
Module: print_state

This module prints the State object with the provided
name from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password db_name state_name".format(sys.argv[0]))
    else:
        username, password, db_name, state_name = \
                sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

        # Create an engine to establish a connection to the MySQL database
        engine = create_engine('mysql+mysqldb://{}:{}\
                @localhost:3306/{}'.format(username, password, db_name))

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Query State object based on the provided state name
        state = session.query(State).filter(State.name == state_name).first()

        # Display results as per requirement
        if state:
            print(state.id)
        else:
            print("Not found")

        # Close the session
        session.close()
