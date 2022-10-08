#!/usr/bin/python3
"""This module contains a script that lists
    all cities from the database hbtn_0e_4_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
    cities INNER JOIN states ON
    cities.state_id = states.id ORDER BY cities.id ASC""")

    results = cur.fetchall()

    for result in results:
        print("(%s, '%s', '%s')" % (result[0], result[1], result[2]))
