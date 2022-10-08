#!/usr/bin/python3
"""
This module contains a script that
adds the State object “Louisiana” to the
database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine, insert
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana_state = State(name="Louisiana")
    session.add(louisiana_state)

    louisiana_state_id = session.query(State).\
        filter(State.name == 'Louisiana').first()
    session.commit()
    print(louisiana_state_id.id)

    Base.metadata.create_all(engine)
