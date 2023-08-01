from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "users"

    username = db.Column(
        db.String(20),
        primary_key=True
    )

    password = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    first_name = db.Column(
        db.String(30),
        nullable=False
    )

    last_name = db.Column(
        db.String(30),
        nullable=False
    )

    @classmethod
    def register(cls, username, password):
        """ register user with hashed password & return user"""

        hashed = bcrypt.generate_password_hash(password).decode('utf8')

        return cls(username=username, password=hashed)

def connect_db(app):
    """Connect this database to provided Flask app"""

    app.app_context().push()
    db.app = app
    db.init_app(app)
