from flask import Flask

from routes import register_blueprints

app = Flask(__name__)

register_blueprints(app)

@app.route('/')
def home():
    return 'Hello World'
