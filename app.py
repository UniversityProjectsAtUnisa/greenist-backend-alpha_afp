from src.views import app
from src.models import db
from config import DB_URL

db.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


# cli commands
@app.cli.command('resetdb')
def resetdb_command():
    """Destroys and creates the database + tables."""

    from sqlalchemy_utils import database_exists, create_database, drop_database
    if database_exists(DB_URL):
        print('Deleting database.')
        drop_database(DB_URL)
    if not database_exists(DB_URL):
        print('Creating database.')
        create_database(DB_URL)

    print('Creating tables.')
    db.create_all()
    print('ResetDB completed')
