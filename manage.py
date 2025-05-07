from flask.cli import FlaskGroup

from src import app, db
from src.accounts.models import User

cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()