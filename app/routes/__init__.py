from app.routes.listings import listings


def register_blueprints(app):
    app.register_blueprint(listings, url_prefix='/listings')