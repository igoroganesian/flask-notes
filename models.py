"""Models for Notes App"""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

db = SQLAlchemy()

class User(db.Model):
    """ class for User instance with password, email, first and last name;
        username as primary key """

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

    notes = db.relationship('Note', backref='user')

    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        """ register user with hashed password & return user instance """

        hashed = bcrypt.generate_password_hash(password).decode('utf8')

        return cls(
            username=username,
            password=hashed,
            email=email,
            first_name=first_name,
            last_name=last_name
            )


    @classmethod
    def authenticate(cls, username, password):
        """ authenticates username and password;
            returns user instance or False"""

        u = cls.query.filter_by(username=username).one_or_none()

        if u and bcrypt.check_password_hash(u.password, password):
            return u
        else:
            return False


class Note(db.Model):

    __tablename__ = "notes"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    title = db.Column(
        db.String(100),
        nullable=False
    )

    content = db.Column(
        db.Text,
        nullable=False
    )

    owner_username = db.Column(
        db.ForeignKey("users.username")
    )


def connect_db(app):
    """Connect this database to provided Flask app"""

    app.app_context().push()
    db.app = app
    db.init_app(app)
