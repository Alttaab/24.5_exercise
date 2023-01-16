"""Models for Flask User Feedback App"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User."""
    
    __tablename__ = "users"
    
    username = db.Column(db.String(20),
                   primary_key=True,
                   nullable=False,
                   unique=True)
    
    password = db.Column(db.Text,
                   nullable=False,
                   unique=True)
    
    email = db.Column(db.String(50),
                   nullable=False,
                   unique=True)
    
    first_name = db.Column(db.String(30),
                   nullable=False,
                   unique=True)
    
    last_name = db.Column(db.String(30),
                   nullable=False,
                   unique=True)
    