#!/usr/bin/python3

"""
script that lists all State objects that contain the letter a
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')

    session = sessionmaker(bind=engine)
    session = session()

    states = session.query(State).filter(State.name.contains('a')).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
