#!/usr/bin/python3
"""
Module: add_state

This module adds the State object "Louisiana" to the
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

        # Create a new State object for Louisiana
        new_state = State(name="Louisiana")

        # Add new State object to d session & commit changes to d database
        session.add(new_state)
        session.commit()

        # Print the new state's ID
        print(new_state.id)

        # Close the session
        session.close()
