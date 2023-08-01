from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, URL



class CreateUserForm(FlaskForm):
    """ form for creating User instance """

    username = StringField("Username",
                           validators=[InputRequired()])
    password = PasswordField("Password",
                            validators=[InputRequired()])
    email = StringField("Email url",
                        validators=[InputRequired(), URL()])
    first_name = StringField("First name",
                           validators=[InputRequired()])
    last_name = StringField("Last name",
                           validators=[InputRequired()])