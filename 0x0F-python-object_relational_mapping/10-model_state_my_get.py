#!/usr/bin/python3
"""
This module contains a script that
a script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa

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

    result = session.query(State).filter(State.name == sys.argv[4]).first()

    if result:
        print('{}'.format(result.id))
    else:
        print('Not found')

    Base.metadata.create_all(engine)
