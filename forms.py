"""Forms for Notes App"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length


class CreateUserForm(FlaskForm):
    """ form for creating User instance """

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)]
    )
    password = PasswordField("Password",
        validators=[InputRequired(), Length(min=6, max=100)]
    )
    email = StringField("Email url",
                        validators=[InputRequired(), Email(), Length(min=7,max=50)])
    first_name = StringField("First name",
                           validators=[InputRequired(), Length(min=1, max=30)])
    last_name = StringField("Last name",
                           validators=[InputRequired(), Length(min=1, max=30)])


class UserLoginForm(FlaskForm):
    """ form for logging in User instance """

    username = StringField("Username",
                           validators=[InputRequired(), Length(min=1, max=20)])
    password = PasswordField("Password",
                            validators=[InputRequired(), Length(min=6, max=100)])

class CSRFForm(FlaskForm):
    """ form for CSRF protection """