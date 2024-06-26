#!/usr/bin/python3
import sys
import MySQLdb
"""
script that lists all states from the database
"""


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
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()
