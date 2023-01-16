"""Forms for user feedback app."""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField,FloatField, SelectField
from wtforms.validators import InputRequired, Optional, Email

class UserRegisterForm(FlaskForm):
    """Form for registering a new user."""
    
    username = StringField("Username")
    password = PasswordField("Password")
    email = EmailField("Email")
    first_name = StringField("First Name")
    last_name = StringField("Last Name")