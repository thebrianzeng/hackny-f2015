from flask import Blueprint, request, render_template, redirect, jsonify

from app.schema import db, Listing

listings_blueprint = Blueprint('listings_blueprint', __name__)


@listings_blueprint.route('/', methods=['GET', 'POST'])
def create_listing():
    if request.method == 'POST':
        listing = Listing()
        listing.update(request.form)

        db.session.add(listing)
        db.session.commit()

        return redirect('/')
    elif request.method == 'GET':
        listings = Listing.query.filter(Listing.sold == False).all()
        json_list = {'listings': [listing.serialize for listing in listings]}
        return jsonify(json_list)
    return 'failed to create listing'

@listings_blueprint.route('/create/')
def create_listing_page():
    return render_template('create_listing.html')


@listings_blueprint.route('/<int:listing_id>')
def get_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    return 'found listing ' + listing.id


@listings_blueprint.route('/<int:listing_id>/update', methods=['POST'])
def update_listing(listing_id):
    if request.method == 'POST':
        listing = Listing.query.get_or_404(listing_id)
        listing.update(request.form)
        db.session.add(listing)
        db.session.commit()
        return 'updated listing ' + listing_id
    return 'failed to update listing'


@listings_blueprint.route('/<listing_id>/delete')
def delete_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    db.session.delete(listing)
    db.session.commit()
    return 'deleted listing ' + listing_id
#
#
# @listings_blueprint.route('/<listing_id>/purchase', methods=['POST'])
# def purchase_meal(listing_id):
#     if request.method == 'POST':  # probably unnecessary
#         transactions.handle_purchase(listing_id, request.form)
#         # TODO: send a success response
#         # TODO: Alert the seller
#
#
# @listings_blueprint.route('/<listing_id>/complete')
# def complete_transaction(listing_id):
#     transactions.complete_transaction(listing_id)
#
#
# @listings_blueprint.route('/test_stripe')
# def test_stripe():
#     transactions.test_stripe()

