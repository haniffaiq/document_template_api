from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from sqlalchemy import text

db = SQLAlchemy()

def test_db_connection():
    try:
        db.session.execute(text('SELECT 1'))
        return True
    except OperationalError:
        return False
