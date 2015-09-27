import json

from flask import Flask, render_template, request, redirect, session
from sqlalchemy.orm import joinedload
import httplib2

from oauth2client.client import OAuth2WebServerFlow

app = Flask(__name__)

from schema import db, Listing, User
from routes import register_blueprints
from config import flask_config

OAUTH_REDIRECT_URI = 'http://localhost:' + '5000' + \
                     '/oauth2callback'

flow = None

app.config.from_object(flask_config)
register_blueprints(app)
db.create_all()

SCOPES = 'https://www.googleapis.com/auth/userinfo.email'
CLIENT_ID = app.config['CLIENT_ID']
CLIENT_SECRET = app.config['CLIENT_SECRET']

@app.route('/')
def home():
    listings = Listing.query.filter(Listing.sold == False).all()
    return render_template("browse.html", listings=listings)


def create_flow():
    global flow
    flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
                               client_secret=CLIENT_SECRET,
                               scope=SCOPES,
                               redirect_uri=OAUTH_REDIRECT_URI)


def get_auth_uri():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    return flow.step1_get_authorize_url()


def create_user(email):
    user = User(email=email)
    db.session.add(user)
    db.session.commit()
    return user


def get_user(email):
    user = User.query.filter_by(email=email).first()
    return user

@app.route('/logout')
def logout():
    session.pop('email')
    return redirect('/')


@app.route('/oauth')
def oauth():
    create_flow()
    auth_uri = get_auth_uri()
    return redirect(auth_uri)


@app.route('/oauth2callback')
def oauth2callback():
    code = request.args.get('code')
    credentials = flow.step2_exchange(code)
    http = httplib2.Http()
    http = credentials.authorize(http)
    resp, content = http.request(
        'https://www.googleapis.com/oauth2/v1/userinfo?alt=json', 'GET')
    response_data = json.loads(content)
    email = response_data['email']

    user = get_user(email)
    if not user:
        user = create_user(email)
    session['email'] = user.email
    session['user_id'] = user.id

    user_path = '/users/' + str(user.id) + '/listings'
    return redirect(user_path)

