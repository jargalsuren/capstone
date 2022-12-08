from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    ingredient = db.Column(db.String(50), nullable=False)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False, nullable=False)
    category = db.Column(db.String(20))
    photo = db.Column(db.String(100))
    duration = db.Column(db.Integer, unique=False)
    instruction = db.Column(db.String(10000), nullable=True)


