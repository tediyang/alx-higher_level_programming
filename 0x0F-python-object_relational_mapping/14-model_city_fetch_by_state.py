#!/usr/bin/python3
"""Import modules"""

from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import create_engine


def main(argv):
    """ create the table in the database and print instances."""
    URL = f"""mysql+mysqldb://{argv[1]}:{argv[2]}
            @localhost/{argv[3]}"""
    engine = create_engine(URL, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State, City).join(City.state_id, State.id).order_by(City.id)
    for c, s in rows:
        print(f"{s.name}: ({c.id}) {c.name}")
    session.close()


if __name__ == "__main__":
    main(sys.argv)
