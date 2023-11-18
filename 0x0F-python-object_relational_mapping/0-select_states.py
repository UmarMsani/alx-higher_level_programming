#!/usr/bin/python3
"""
Module: 0-select_states

This module lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

def list_states(username, password, db_name):
    """
    Lists all states from the specified database.

    Args:
    - username (str): MySQL username.
    - password (str): MySQL password.
    - db_name (str): Database name to connect to.
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password db_name".format(sys.argv[0]))
    else:
        username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
        list_states(username, password, db_name)
