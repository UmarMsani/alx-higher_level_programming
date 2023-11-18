#!/usr/bin/python3
"""
Module: safe_search_states

This module safely searches and displays values in the states table
of hbtn_0e_0_usa where name matches the provided argument.
"""

import sys
import MySQLdb


def safe_search_states(username, password, db_name, state_name):
    """
    Safely searches and displays values in the states table
    where name matches the provided state_name.

    Args:
    - username (str): MySQL username.
    - password (str): MySQL password.
    - db_name (str): Database name to connect to.
    - state_name (str): State name to search for in the database.
    """
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

        # Prepare a parameterized query to safely search for the state_name
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

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
    if len(sys.argv) != 5:
        print("Usage: {} \
                username password db_name state_name".format(sys.argv[0]))
    else:
        username, password, db_name, state_name = \
                sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        safe_search_states(username, password, db_name, state_name)
