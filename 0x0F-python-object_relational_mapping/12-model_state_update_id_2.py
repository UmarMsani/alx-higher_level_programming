#!/usr/bin/python3
"""
Module: update_state_name

This module changes the name of a State object from the
database hbtn_0e_6_usa.
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

        # Query the State object with id = 2
        state_to_update = session.query(State).filter_by(id=2).first()

        # Update the name of the State to 'New Mexico' if it exists
        if state_to_update:
            state_to_update.name = 'New Mexico'
            session.commit()
        else:
            print("State with ID 2 not found")

        # Close the session
        session.close()
