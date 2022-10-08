#!/usr/bin/python3
"""
This module contains a script that
prints the first State object from the database
hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).first()

    if result:
        print('%s: %s' % (result.id, result.name))
    else:
        print('Nothing')

    Base.metadata.create_all(engine)
