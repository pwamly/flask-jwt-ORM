import click
from flask.cli import with_appcontext

from .extensions import db
from .models import  Users

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
    
@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()