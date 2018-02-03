#!/usr/bin/env python
# coding=utf-8
"""This is a simple example of using SQLAlchemy in ORM mode to work with a PostgreSQL database.
"""
import getpass

import colorama
from colorama import Fore
import sqlalchemy as sa
import sqlalchemy.ext.declarative as sa_decl
import sqlalchemy.orm as sa_orm

# Classes mapped using the Declarative system are defined in terms of a base class which maintains a catalog of
# classes and tables relative to that base - this is known as the declarative base class
Base = sa_decl.declarative_base()

# We define a Session class which will serve as a factory for new Session objects
Session = sa_orm.sessionmaker()


class User(Base):
    """Now that we have a “base”, we can define any number of mapped classes in terms of it.

    We will start with just a single table called users, which will store records for the end-users using our
    application. A new class called User will be the class to which we map this table.  Within the class, we define
    details about the table to which we’ll be mapping, primarily the table name, and names and datatypes of columns.
    """
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    fullname = sa.Column(sa.String)
    password = sa.Column(sa.String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


if __name__ == '__main__':
    colorama.init(autoreset=True)

    # Convert SQLAlchemy Version to a float, make sure it is at least 1.0.15, and print version out
    sa_ver = float('{}.{}{}'.format(*sa.__version__.split('.')))
    assert sa_ver >= 1.015
    print(Fore.LIGHTBLUE_EX + 'Using SQLAlchemy version {}'.format(sa.__version__))

    # User name and password for the PostgreSQL server
    db_user = getpass.getuser()
    db_pass = getpass.getpass(prompt="{}'s PostgreSQL password: ".format(db_user))

    # PostgreSQL server host:port - if the port is the default of 5432, then it can be left off
    host = 'localhost'

    # # WARNING: This database must already exist in the PostgreSQL server.  It may or may not contain any tables.
    database = 'sample_db'

    # Use a SQLite database stored in the 'foo.db' file (set echo to True for SQLAlchemy debug output)
    engine = sa.create_engine('postgresql://{}:{}@{}/{}'.format(db_user, db_pass, host, database), echo=False)

    # Create the schema - make sure the table exists
    Base.metadata.create_all(engine)

    # Connect the engine to the Session factory
    Session.configure(bind=engine)

    # Create a session
    session = Session()

    # Query users table to see if ed already exists
    existing_user = session.query(User).filter_by(name='ed').first()

    if existing_user is None:
        # Add an object to the database
        ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
        session.add(ed_user)
        session.commit()

        # Query user
        our_user = session.query(User).filter_by(name='ed').first()
        assert our_user is ed_user
        print('User added to the database: {!r}'.format(ed_user))
    else:
        print('User already exists in the database: {!r}'.format(existing_user))

    # Close the session
    session.close()

