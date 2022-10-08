#!/usr/bin/python3
"""This module contains a script that takes
    in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name
    matches the argument and is safe from SQL injections
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, db=sys.argv[3],
                         user=sys.argv[1], passwd=sys.argv[2])
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
    cities INNER JOIN states ON
    cities.state_id = states.id WHERE states.name = %s
    ORDER BY cities.id ASC""", (sys.argv[4], ))

    results = cur.fetchall()

    print(', '.join('{}'.format(result[0]) for result in results))
