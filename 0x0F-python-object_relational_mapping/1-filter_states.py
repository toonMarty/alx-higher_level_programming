#!/usr/bin/python3
"""This module contains a script that filters
    all states with a name starting with N
    from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    MySQLdb.connect(user=sys.argv[1])
    MySQLdb.connect(passwd=sys.argv[2])
    MySQLdb.connect(db=sys.argv[3])

    db = MySQLdb.connect(host="localhost", port=3306, db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC """)

    results = cur.fetchall()

    for result in results:
        print("(%s, '%s')" % (result[0], result[1]))
