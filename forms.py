"""Forms for Notes App"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email


class CreateUserForm(FlaskForm):
    """ form for creating User instance """

    username = StringField(
        "Username",
        validators=[InputRequired()]
    )
    password = PasswordField("Password",
        validators=[InputRequired()]
    )
    email = StringField("Email url",
                        validators=[InputRequired(), Email()])
    first_name = StringField("First name",
                           validators=[InputRequired()])
    last_name = StringField("Last name",
                           validators=[InputRequired()])
    #TODO: add length validators


class UserLoginForm(FlaskForm):
    """ form for logging in User instance """

    username = StringField("Username",
                           validators=[InputRequired()])
    password = PasswordField("Password",
                            validators=[InputRequired()])

class CSRFForm(FlaskForm):
    """ form for CSRF protection """