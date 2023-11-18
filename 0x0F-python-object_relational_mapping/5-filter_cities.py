#!/usr/bin/python3
"""
Module: cities_by_given_state

This module lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def cities_by_given_state(username, password, db_name, state_name):
    """
    Lists all cities of a given state from the specified database.

    Args:
    - username (str): MySQL username.
    - password (str): MySQL password.
    - db_name (str): Database name to connect to.
    - state_name (str): Name of the state to search for cities.
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

            # Prepare a parameterized query to safely search for cities of the given state
            query = "SELECT cities.name " \
                    "FROM cities JOIN states ON cities.state_id = states.id " \
                    "WHERE states.name = %s " \
                    "ORDER BY cities.id ASC"

            cursor.execute(query, (state_name,))

            # Fetch all rows returned by the query
            rows = cursor.fetchall()

            # Display results as per requirement (only city names)
            city_names = [row[0] for row in rows]  # Extract city names from the result
            print(", ".join(city_names))  # Display city names separated by comma

            # Close cursor and connection
            cursor.close()
            db.close()
        except MySQLdb.Error as e:
            print("MySQL Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password db_name state_name".format(sys.argv[0]))
    else:
        username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        cities_by_given_state(username, password, db_name, state_name)
