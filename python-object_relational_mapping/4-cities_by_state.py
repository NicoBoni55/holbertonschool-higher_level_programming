#!/usr/bin/python3

"""
    script that lists all states from the database
"""

import sys
import MySQLdb


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 ORDER BY cities.state_id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
