#!/usr/bin/python3

"""
script that changes the name of a State
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')

    session = sessionmaker(bind=engine)
    session = session()

    update_state = session.query(State).filter_by(id = 2).first()
    
    if update_state:
        update_state.name = "New Mexico"
        session.commit()

    session.close()