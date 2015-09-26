from __future__ import print_function, division

from flask_sqlalchemy import SQLAlchemy

from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../db.db"
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    listings = db.relationship("Listing", backref="user", lazy="dynamic")

    email = db.Column(db.String(80), unique=True)

class Listing(db.Model):
    __tablename__ = "listing"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    price = db.Column(db.DECIMAL(precision=2, asdecimal=True), nullable=False)
    description = db.Column(db.String, nullable=False)
    sold = db.Column(db.Boolean, default=False, nullable=False)
