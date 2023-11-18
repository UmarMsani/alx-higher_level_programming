#!/usr/bin/python3
"""
Module: list_states_starting_with_N

This module lists all states with a name starting
with 'N' from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


def list_states_starting_with_N(username, password, db_name):
    """
    Lists all states starting with 'N' from the specified database.

    Args:
    - username (str): MySQL username.
    - password (str): MySQL password.
    - db_name (str): Database name to connect to.
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

        # Execute a SELECT query for states starting with 'N'
        cursor.execute(
                "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
                )

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
        list_states_starting_with_N(username, password, db_name)
