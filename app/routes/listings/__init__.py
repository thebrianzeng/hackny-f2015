from flask import Blueprint, request

listings = Blueprint('listings', __name__)


@listings.route('/', methods=['POST'])
def create_listing():
    if request.method == 'POST':
        listings_db.create_listing(request.form)
        return 'created_listing'
    return 'failed to create listing'


@listings.route('/<listing_id>')
def get_listing(listing_id):
    listing = listings_db.find_listing(listing_id)
    return 'found listing ' + listing.id


@listings.route('/<listing_id>/update', methods=['POST'])
def update_listing(listing_id):
    if request.method == 'POST':
        listings_db.update_listing(listing_id, request.form)
        return 'updated listing ' + listing_id
    return 'failed to update listing'


@listings.route('/<listing_id>/delete')
def delete_listing(listing_id):
    listings_db.delete_listing(listing_id)
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

