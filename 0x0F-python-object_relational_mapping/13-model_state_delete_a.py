#!/usr/bin/python3
"""
Module: delete_states_with_a

This module deletes State objects with a name containing the
letter 'a' from the database hbtn_0e_6_usa.
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

        # Query and delete State objects with a name containing the letter 'a'
        states_to_delete = session.query(State)
        states_to_delete = states_to_delete.filter(State.name.like('%a%'))
        states_to_delete = states_to_delete.all()
        for state in states_to_delete:
            session.delete(state)

        # Commit changes to the database
        session.commit()

        # Close the session
        session.close()
