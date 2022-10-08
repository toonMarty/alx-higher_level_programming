#!/usr/bin/python3
"""This module contains a script that takes
    in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name
    matches the argument.
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, db=sys.argv[3],
                         user=sys.argv[1], passwd=sys.argv[2])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'"
                "ORDER BY states.id ASC".format(sys.argv[4])
    results = cur.fetchall()

    for result in results:
        print("(%s, '%s')" % (result[0], result[1]))
