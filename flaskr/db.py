import sqlite3
import click
from flask import current_app, g


def get_db():
    """Connect to database if not already connected in request"""
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types = sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    """Close connection to database"""
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    """Initialize database connection and execute scripts"""
    db = get_db()

    with current_app.open_resource('schema.sql') as file:
        db.executescript(file.read().decode('utf-8'))

@click.command('init_db')
def init_db_cli_command():
    """Init database and display sucess message in cli"""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    """Initialize app with teardown and cli commands"""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_cli_command)
