#!/usr/bin/env python3
# coding=utf-8
"""This is a simple example of using SQLAlchemy in ORM mode to work with a PostgreSQL database.
"""
import getpass
import logging
import sys

import colorama
from colorama import Fore
import sqlalchemy as sa                         # SQLAlchemy
import sqlalchemy.exc as sa_exc                 # SQLAlchemy Exceptions
import sqlalchemy.ext.declarative as sa_decl    # SQLAlchemy Declarative
import sqlalchemy.orm as sa_orm                 # SQLAlchemy ORM
import sqlalchemy_utils as sa_utils

logger = logging.getLogger(__name__)


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
    id = sa.Column(sa.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = sa.Column(sa.String(50), nullable=False)
    fullname = sa.Column(sa.String(80), unique=True)
    password = sa.Column(sa.String(30))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Address(Base):
    """Let’s consider how a second table, related to User, can be mapped and queried.

    Users in our system can store any number of email addresses associated with their username. This implies a basic one
    to many association from the users to a new table which stores email addresses, which we will call addresses.
    """
    __tablename__ = 'addresses'
    id = sa.Column(sa.Integer, primary_key=True)
    email_address = sa.Column(sa.String(60), nullable=False)
    # ForeignKey construct is a directive that constrains values in this column to be present in the named remote column
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))

    user = sa_orm.relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


# Users in our system can store any number of email addresses associated with their username
User.addresses = sa_orm.relationship("Address", order_by=Address.id, back_populates="user")


def check_db_schema(declarative_base, sa_session):
    """Check whether the current database matches the models declared in model base.

    Checks to make sure all tables exist and that each table contains columns with the expected name.

    What is not checked:
    * Column types are not verified
    * Relationships are not verified at all (TODO)

    :param declarative_base: Declarative Base for SQLAlchemy models to check
    :param sa_session: SQLAlchemy session bound to an engine
    :return: True if all declared models have corresponding tables and columns
    """
    sa_engine = sa_session.get_bind()
    iengine = sa.inspect(sa_engine)

    errors = False

    tables = iengine.get_table_names()

    # Go through all SQLAlchemy models
    for name, klass in declarative_base._decl_class_registry.items():

        if isinstance(klass, sa_decl._ModuleMarker):
            # Not a model
            continue

        table = klass.__tablename__
        if table in tables:
            # Check all columns are found
            # Looks like [{'default': "nextval('sanity_check_test_id_seq'::regclass)", 'autoincrement': True, 'nullable': False, 'type': INTEGER(), 'name': 'id'}]

            columns = [c["name"] for c in iengine.get_columns(table)]
            mapper = sa.inspect(klass)

            for column_prop in mapper.attrs:
                if isinstance(column_prop, sa_orm.RelationshipProperty):
                    # TODO: Add sanity checks for relations
                    pass
                else:
                    for column in column_prop.columns:
                        # Assume normal flat column
                        if not column.key in columns:
                            logger.error("Model %s declares column %s which does not exist in database %s", klass, column.key, sa_engine)
                            errors = True
        else:
            logger.error("Model %s declares table %s which does not exist in database %s", klass, table, sa_engine)
            errors = True

    return not errors


if __name__ == '__main__':
    colorama.init(autoreset=True)

    # Convert SQLAlchemy Version to a float, make sure it is at least 1.0.15, and print version out
    sa_ver = float('{}.{}{}'.format(*sa.__version__.split('.')))
    assert sa_ver >= 1.015
    print(Fore.LIGHTBLUE_EX + 'Using SQLAlchemy version {}'.format(sa.__version__))

    # PostgreSQL server host:port - if the port is the default of 5432, then it can be left off
    host = 'localhost'

    # User name and password for the PostgreSQL server
    db_user = getpass.getuser()
    db_pass = getpass.getpass(prompt="{}'s password for PostgreSQL server {!r}: ".format(db_user, host))

    # Database to connect to within the PostgreSQL server.  It may or may not contain any tables.
    database = 'sample_db'
    if len(sys.argv) > 1:
        database = sys.argv[1]

    #  The string form of the URL is ``dialect[+driver]://user:password@host:port/dbname[?key=value..]``
    db_url = 'postgresql://{}:{}@{}/{}'.format(db_user, db_pass, host, database)

    # Try connecting to the server to check to see if the DB exists and our the URL and credentials are good
    try:
        db_exists = sa_utils.database_exists(db_url)
    except sa_exc.OperationalError as err:
        print(Fore.RED + 'Failed to connect to PostgreSQL server {!r} as user {!r}: {}'.format(host, db_user, err))
        sys.exit(1)

    # Check to see if the database exists
    validate_shema = False
    if db_exists:
        # Warn the user that the DB exists and ask if they would like to delete it and recreate it or move on?
        print(Fore.YELLOW + 'Database {!r} already exists'.format(database))
        recreate = input('Would you like to delete database {!r} and recreate it from scratch (y/n)? ')
        if recreate.lower().startswith('y'):
            # Issue the appropriate DROP DATABASE statement to delete the database
            sa_utils.drop_database(db_url)
            # Issue the appropriate CREATE DATABASE statement to recreate an empty database
            sa_utils.create_database(db_url)
        else:
            print('You elected not to recreate database {!r}, the schema will be validated ...'.format(db_url))
            validate_shema = True
    else:
        # Create the database from scratch
        print(Fore.YELLOW + 'Database {!r} does not exist, so creating it ...'.format(database))
        # Issue the appropriate CREATE DATABASE statement to create an empty database
        sa_utils.create_database(db_url)

    # Use a SQLite database stored in the 'foo.db' file (set echo to True for SQLAlchemy debug output)
    engine = sa.create_engine(db_url, echo=False)

    # Create the schema - make sure the tables exist
    Base.metadata.create_all(engine)

    # Connect the engine to the Session factory
    Session.configure(bind=engine)

    # Create a session
    session = Session()

    # Validate the schema if the database already existed and the user opted not to recreate it from scratch
    if validate_shema:
        pass
        # if check_db_schema(Base, session):
        #     print(Fore.LIGHTGREEN_EX + 'Existing DB schema looks OK')
        # else:
        #     print(Fore.RED + 'Existing DB schema conflicts with expected schema, database needs to be recreated')
        #     sys.exit(2)

    # Configure details for a user
    user_name = 'todd'
    full_name = 'Todd Leonhardt'
    password = 'password'

    # Query users table to see if ed already exists
    existing_user = session.query(User).filter_by(name=user_name).first()

    if existing_user is None:
        # Add an object to the database
        new_user = User(name=user_name, fullname=full_name, password=password)
        session.add(new_user)
        session.commit()

        # Query user
        our_user = session.query(User).filter_by(name=user_name).first()
        assert our_user is new_user
        print('User added to the database: {!r}'.format(new_user))
    else:
        print('User already exists in the database: {!r}'.format(existing_user))

    # Close the session
    session.close()

