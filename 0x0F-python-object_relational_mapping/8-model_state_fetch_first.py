#!/usr/bin/python3
"""Alchemy query state-id = 1"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    my_state = session.query(State).first()
    if (my_state is None):
        print("Nothing")
    else:
        print(my_state.id, my_state.name)
    session.close()
