"""Models for Flask User Feedback App"""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
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
    
    @classmethod
    def register(cls, username, password, first_name, last_name, email):
        
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        
        user = cls(
            username=username,
            password=hashed_utf8,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        db.session.add(user)
        return user
    
    @classmethod
    def authenticate(cls, username, password):
        user = User.query.filter_by(username=username).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        
        else:
            return False
        
        


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)