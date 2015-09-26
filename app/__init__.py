from flask import Flask

app = Flask(__name__)

from schema import db
from routes import register_blueprints

register_blueprints(app)

@app.route('/')
def home():
    return 'Hello World'
