from app.routes.auth import auth
from app.routes.listings import listings


def register_blueprints(app):
    app.register_blueprint(listings, url_prefix='/listings')
    app.register_blueprint(auth, url_prefix='/auth')
