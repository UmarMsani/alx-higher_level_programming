#!/usr/bin/python3
"""
Module: 14-model_city_fetch_by_state

Prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

        # Query City and State objects, join them and fetch the results
        cities = session.query(City, State).join(State).order_by(City.id).all()

        # Print results as per the format
        for city, state in cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

        # Close the session
        session.close()
