from flask import Flask, redirect, render_template, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User
from forms import UserRegisterForm

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
    """Generates a for and accepts form submissions"""
    
    form = UserRegisterForm()
    
    if form.validate_on_submit():
        
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        
        user = User.register(username, password, first_name, last_name, email)
        
        db.session.commit()
        
        return redirect("/")
    
    else:
        return render_template("users/register.html",form=form)
    
    return 'placeholder'
    #TODO: add register path

@app.route("/login",methods=["GET","POST"])
def login_user():
    return 'placeholder'
    #TODO: add login path

@app.route("/secret")
def secret():
    return 'You made it!'
    #TODO: add secret path