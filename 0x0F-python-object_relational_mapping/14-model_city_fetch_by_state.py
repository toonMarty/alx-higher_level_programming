#!/usr/bin/python3
"""
This module contains a script that lists all
City objects from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state_instance, city_instance in \
            session.query(State, City).filter(State.id == City.state_id). \
            order_by(State.id.asc()):
        print('%s: (%s) %s' %
              (state_instance.name, city_instance.id, city_instance.name))

    Base.metadata.create_all(engine)
