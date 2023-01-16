"""Forms for user feedback app."""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField,FloatField, SelectField
from wtforms.validators import InputRequired, Length,Optional, Email

class UserRegisterForm(FlaskForm):
    """Form for registering a new user."""
    
    username = StringField("Username",
                           validators=[InputRequired(), Length(min=1, max=20)])
    password = PasswordField("Password",
                           validators=[InputRequired(), Length(min=1, max=50)])
    email = EmailField("Email")
    first_name = StringField("First Name",
                           validators=[InputRequired(), Length(min=1, max=30)])
    last_name = StringField("Last Name",
                           validators=[InputRequired(), Length(min=1, max=30)])

class UserLoginForm(FlaskForm):
    """Form for logging in a user."""
    
    username = StringField("Username",
                           validators=[InputRequired(), Length(min=1, max=20)])
    password = PasswordField("Password",
                           validators=[InputRequired(), Length(min=1, max=50)])

class UserLoginForm(FlaskForm):
    """Form for logging in a user."""
    
    username = StringField("Username",
                           validators=[InputRequired(), Length(min=1, max=20)])
    password = PasswordField("Password",
                           validators=[InputRequired(), Length(min=1, max=50)])
        
class DeleteForm(FlaskForm):
    """
        
    """