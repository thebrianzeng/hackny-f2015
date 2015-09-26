from flask import Flask, render_template, request, redirect
from sqlalchemy.orm import joinedload
import httplib2

from oauth2client.client import OAuth2WebServerFlow

app = Flask(__name__)

from schema import db, Listing, User
from routes import register_blueprints


OAUTH_REDIRECT_URI = 'http://localhost:' + '5000' + \
                     '/oauth2callback'

# CLIENT_ID = app.config['CLIENT_ID']
# CLIENT_SECRET = app.config['CLIENT_SECRET']

flow = None


register_blueprints(app)
db.create_all()

@app.route('/')
def home():
    listings = Listing.query.options(joinedload("user")) \
                            .filter(Listing.sold == False).all()
    return render_template("browse.html", listings=listings)

#
# def create_flow():
#     global flow
#     flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
#                                client_secret=CLIENT_SECRET,
#                                redirect_uri=OAUTH_REDIRECT_URI)
#
#
# def get_auth_uri():
#     """Gets valid user credentials from storage.
#
#     If nothing has been stored, or if the stored credentials are invalid,
#     the OAuth2 flow is completed to obtain the new credentials.
#
#     Returns:
#         Credentials, the obtained credential.
#     """
#     return flow.step1_get_authorize_url()
#
# @app.route('/oauth')
# def oauth():
#     create_flow()
#     auth_uri = get_auth_uri()
#     return redirect(auth_uri)
#
# @app.route('/oauth2callback')
# def oauth2callback():
#     code = request.args.get('code')
#     credentials = flow.step2_exchange(code)
#     http = httplib2.Http()
#     http = credentials.authorize(http)
#
#     return 'Got credentials'

