"""
This is not from a Django project. This file is used
to run management commands.
"""

import os

import click

from api.database import db
from api.database.models.images import Image


models = [
    Image
]


@click.group()
def cmds():
    pass


@click.group()
def database():
    pass


@click.command(help="Create tables")
def maketables():
    click.echo("Creating tables...")
    
    db.connect()
    db.create_tables(models)

    click.echo("Tables created")

@click.command(help="Delete database and recreate tables")
@click.option('--confirm', prompt=True, default="No")
def reset(confirm):
    if confirm.lower() == 'yes':
        click.echo("Reseting database...")
        
        with open('db.sqlite3', 'w') as f:
            f.write('')
            f.close()
    
        db.connect()
        db.create_tables(models)
    
        click.echo("Database recreated successfully.")
    else:
        click.echo("Cancelled.")

@click.group()
def images():
    pass

@click.command(help="Update images database")
def update():
    for path, subdirs, files in os.walk("media/images/"):
        for name in files:
            try:
                Image.create(file_path=os.path.join(path, name), category=Image.Category(path.split('/', 2)[2]).value)
                click.echo(f"Addded image {os.path.join(path, name)}")
            except Exception as e:
                click.echo(f"Skipping existent image {os.path.join(path, name)}")

@click.command(help="Rebuild images table")
def rebuild():
    Image.delete().execute()
    for path, subdirs, files in os.walk("media/images/"):
        for name in files:
            Image.create(file_path=os.path.join(path, name), category=Image.Category(path.split('/', 2)[2]).value)
            click.echo(f"Addded image {os.path.join(path, name)}")

database.add_command(maketables)
database.add_command(reset)
images.add_command(update)
images.add_command(rebuild)

cmds.add_command(database)
cmds.add_command(images)

if __name__ == '__main__':
    cmds()
