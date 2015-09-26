from flask import Flask, render_template
from sqlalchemy.orm import joinedload

app = Flask(__name__)

from schema import db, Listing, User
from routes import register_blueprints

register_blueprints(app)
db.create_all()

@app.route('/')
def home():
    listings = Listing.query.options(joinedload("user")) \
                            .filter(Listing.sold == False).all()
    return render_template("browse.html", listings=listings)
