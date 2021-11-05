import sqlite3
from sqlite3.dbapi2 import PARSE_DECLTYPES

import click
from flask import current_app, g
from flask.cli import with_appcontext


def init_app(app):
    # flask will call this function when cleaning up after returning the response
    app.teardown_appcontext(close_db)
    # adds a new command (call via 'flask command_name')
    app.cli.add_command(init_db_command)


# initialize the database
def init_db():
    db = get_db()
    # opens a file with the database
    with current_app.open_resource('schene.sql') as f_db:
        db.executescript(f_db.read().decode('utf8'))


# command line command 'init-db' that initializes the database
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Database initialized.')


# connect to and return the database
def get_db():
    # connection is stored in g
    # connection is reused instead of creating another one if one already exists
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types = sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


# close the database connection
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
