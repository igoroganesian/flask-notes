import os

from flask import Flask, render_template, redirect
# from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, User

from forms import CreateUserForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///???")

app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.get('/')
def show_homepage():
    """ redirects to /register page """

    return redirect('/register')

@app.get('/register')
def show_register_form():
    """ displays user registration form;
    accepts username, password, email, first_name, last_name
    """

    form = CreateUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        new_user = User(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
            )

        db.session.add(new_user)
        db.session.commit()

        return redirect()

    else:
        return render_template("user_add_form.html", form=form)

@app.post('/register')
def process_register_form():
    """ process new user form and redirects to user page """

