#!/usr/bin/python3
import sys
import MySQLdb as engine


def main(argv):
    ''' access a database and prints all the data. '''
    db = engine.connect(host="3306", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    data = cur.execute("SELECT * FROM states")
    for state in data:
        print(state)


if __name__ == "__main__":
    main(sys.argvi)
