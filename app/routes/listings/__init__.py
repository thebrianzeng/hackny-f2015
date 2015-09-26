from flask import Blueprint, request

from app.schema import db, Listing

listings = Blueprint('listings', __name__)


@listings.route('/', methods=['POST'])
def create_listing():
    if request.method == 'POST':
        listing = Listing()
        listing.update(request.form)

        db.session.add(listing)
        db.session.commit()

        return 'created_listing'
    return 'failed to create listing'


@listings.route('/<int:listing_id>')
def get_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    return 'found listing ' + listing.id


@listings.route('/<int:listing_id>/update', methods=['POST'])
def update_listing(listing_id):
    if request.method == 'POST':
        listing = Listing.query.get_or_404(listing_id)
        listing.update(request.form)
        db.session.add(listing)
        db.session.commit()
        return 'updated listing ' + listing_id
    return 'failed to update listing'


@listings.route('/<listing_id>/delete')
def delete_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    db.session.delete(listing)
    db.session.commit()
    return 'deleted listing ' + listing_id
#
#
# @listings.route('/<listing_id>/purchase', methods=['POST'])
# def purchase_meal(listing_id):
#     if request.method == 'POST':  # probably unnecessary
#         transactions.handle_purchase(listing_id, request.form)
#         # TODO: send a success response
#         # TODO: Alert the seller
#
#
# @listings.route('/<listing_id>/complete')
# def complete_transaction(listing_id):
#     transactions.complete_transaction(listing_id)
#
#
# @listings.route('/test_stripe')
# def test_stripe():
#     transactions.test_stripe()

