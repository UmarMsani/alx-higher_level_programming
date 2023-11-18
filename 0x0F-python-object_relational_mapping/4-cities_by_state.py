#!/usr/bin/python3
"""
Module: cities_by_state

This module lists all cities with their respective states
from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def cities_by_state(username, password, db_name):
    """
    Lists all cities with their respective states from
    the specified database.

    Args:
    - username (str): MySQL username.
    - password (str): MySQL password.
    - db_name (str): Database name to connect to.
    """
    if __name__ == "__main__":
        try:
            # Establish a connection to the MySQL database
            db = MySQLdb.connect(
                    host="localhost",
                    port=3306,
                    user=username,
                    passwd=password,
                    db=db_name
                    )

            # Create a cursor object
            cursor = db.cursor()

            # Execute a SELECT query joining cities and states tables
            query = "SELECT cities.id, cities.name, states.name " \
                    "FROM cities JOIN states ON cities.state_id = states.id " \
                    "ORDER BY cities.id ASC"

            cursor.execute(query)

            # Fetch all rows returned by the query
            rows = cursor.fetchall()

            # Display results as per requirement
            for row in rows:
                print(row)

            # Close cursor and connection
            cursor.close()
            db.close()
        except MySQLdb.Error as e:
            print("MySQL Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password db_name".format(sys.argv[0]))
    else:
        username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
        cities_by_state(username, password, db_name)
