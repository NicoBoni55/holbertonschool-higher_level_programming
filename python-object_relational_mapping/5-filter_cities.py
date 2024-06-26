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
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name)
    cur = db.cursor()
    cur.execute("SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') \
                     FROM cities \
                     JOIN states ON cities.state_id = states.id \
                     WHERE states.name = %s \
                     ORDER BY cities.id ASC", [state_name])
    query_rows = cur.fetchone()
    if query_rows and query_rows[0]:
        result = query_rows[0]
        result = result.rstrip(', ')
        print (result)
    cur.close()
    db.close()
