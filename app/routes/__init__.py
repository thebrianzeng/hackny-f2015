from app.routes.auth import auth
from app.routes.listings import listings_blueprint
from app.routes.users import users_blueprint


def register_blueprints(app):
    app.register_blueprint(listings_blueprint, url_prefix='/listings')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(users_blueprint, url_prefix='/users')
