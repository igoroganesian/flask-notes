import os

from flask import Flask, render_template, redirect, session, flash
# Response
# from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, User

from forms import CreateUserForm, UserLoginForm, CSRFForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
# add .env for key!

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///users")

app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.get('/')
def show_homepage():
    """ redirects to /register page """

    return redirect('/register')

@app.route('/register', methods=["GET", "POST"])
def register():
    """display and handle registration form submission;
    accepts username, password, email, first_name, last_name
    """

    form = CreateUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        new_user = User.register(
            username,
            password,
            email,
            first_name,
            last_name
            )

        db.session.add(new_user)
        db.session.commit()

        session["username"] = new_user.username

        return redirect(f'/users/{new_user.username}')

    else:
        return render_template("user_add_form.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Display and handle user login. Accepts username and password. """
    form = UserLoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)

        if user:
            session["username"] = user.username
            return redirect(f'/users/{user.username}')
        else:
            form.username.errors = ["Bad name/password"]

    return render_template('user_login_form.html', form=form)

#TODO: redirect if logged in


@app.get('/users/<username>')
def show_user_info(username):
    """Validate user and if validated, show user info page. Redirect to root
    page if not authorized."""

    form = CSRFForm()

    if "username" not in session:
        flash("You must be logged in to view user page")
        #TODO: forbid other users
        return redirect("/")

    #TODO: import werkzeug errors

    user = User.query.get_or_404(username)
    # breakpoint()
    return render_template('user_info.html', user=user, form=form)

    # \/ if above not an option

    # username = user.username
    # email = user.email
    # first_name = user.first_name
    # last_name = user.last_name

    # user_info = [username, email, first_name, last_name]



@app.post('/logout')
def logout_user():
    """ logs user out and redirects to homepage """

    form = CSRFForm()

    if form.validate_on_submit():
        #TODO: message if invalid
        session.pop("username", None)

    return redirect('/')



