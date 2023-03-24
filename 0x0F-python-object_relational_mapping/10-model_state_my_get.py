#!/usr/bin/python3
"""Import modules"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import create_engine


def main(argv):
    """ create the table in the database and print
        the first instance.
    """
    URL = f"""mysql+mysqldb://{argv[1]}:{argv[2]}
            @localhost/{argv[3]}"""
    engine = create_engine(URL, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State.id).filter(
            State.name=argv[4]).order_by(State.id).first()
    if instance:
        print(instance)
    else:
        print('Not found')
    session.close()


if __name__ == "__main__":
    main(sys.argv)
