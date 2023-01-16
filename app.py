from flask import Flask, redirect, render_template, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User
from forms import UserRegisterForm, UserLoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///user_feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "insecure"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
connect_db(app)
db.create_all()

@app.route("/")
def root():
    """Homepage"""
    return render_template("home.html")

@app.route("/register",methods=["GET","POST"])
def register_user():
    """Generates a form and accepts form submissions"""

    if "username" in session:
        return redirect(f"/users/{session['username']}")
    
    form = UserRegisterForm()
    
    if form.validate_on_submit():
        
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        
        user = User.register(username, password, first_name, last_name, email)
        
        db.session.commit()
        
        session['username'] = user.username
        
        return redirect(f"/users/{session['username']}")
    
    else:
        return render_template("users/register.html",form=form)

@app.route("/login",methods=["GET","POST"])
def login_user():
    """Generates a login form or handles login."""

    if "username" in session:
        return redirect(f"/users/{session['username']}")

    form = UserLoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)  # <User> or False
        if user:
            session['username'] = user.username
            return redirect(f"/users/{user.username}")
        else:
            form.username.errors = ["Invalid username/password."]
            return render_template("users/login.html", form=form)

    return render_template("users/login.html", form=form)

@app.route("/logout")
def logout():
    """Logout route."""

    session.pop("username")
    return redirect("/login")

@app.route("/users/<username>")
def show_user(username):
    return username
    #TODO: add secret path