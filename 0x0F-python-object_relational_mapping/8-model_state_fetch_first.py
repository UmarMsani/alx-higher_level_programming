#!/usr/bin/python3
"""
Module: print_first_state

This module prints the first State object from the database hbtn_0e_6_usa.
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

        # Query the first State object based on states.id
        first_state = session.query(State).order_by(State.id).first()

        # Display the result or print 'Nothing' if the table is empty
        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")

        # Close the session
        session.close()
