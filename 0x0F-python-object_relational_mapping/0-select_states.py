#!/usr/bin/python3
"""
file: 0-select_state.py
Desc: This module contain a script to lists all
states from the database hbtn_0e_0_usa

"""

from sys import argv
import MySQLdb
if __name__=="__main__":
    db = MySQLdb.connect(
            host = "localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cur = bd.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states_info = cur.fetchall()

    for state in states_info:
        print(states)

