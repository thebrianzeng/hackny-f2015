from flask import Blueprint, request, render_template, redirect, jsonify

from app.schema import db, User, Listing

users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/create/')
def create_user_page():
    return render_template('create_user.html')


@users_blueprint.route('/<int:user_id>')
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return user

@users_blueprint.route('/<int:user_id>/listings')
def get_user_listings(user_id):
    listings = Listing.query.filter(Listing.user_id == user_id).filter(
        Listing.sold == False).all()

    return render_template('users_listings.html', listings=listings)


@users_blueprint.route('/<int:user_id>/listings/create', methods=['GET',
                                                                  'POST'])
def create_user_listing(user_id):
    if request.method == 'POST':
        listing = Listing(user_id=user_id)
        listing.update(request.form)

        db.session.add(listing)
        db.session.commit()

        users_listings_path = '/users/' + str(user_id) + '/listings'
        return redirect(users_listings_path)



@users_blueprint.route('/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    if request.method == 'POST':
        user = User.query.get_or_404(user_id)
        user.update(request.form)
        db.session.add(user)
        db.session.commit()
        return 'updated user ' + user_id
    return 'failed to update user'


@users_blueprint.route('/<user_id>/delete')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return 'deleted user ' + user_id
#
#
# @users_blueprint.route('/<user_id>/purchase', methods=['POST'])
# def purchase_meal(user_id):
#     if request.method == 'POST':  # probably unnecessary
#         transactions.handle_purchase(user_id, request.form)
#         # TODO: send a success response
#         # TODO: Alert the seller
#
#
# @users_blueprint.route('/<user_id>/complete')
# def complete_transaction(user_id):
#     transactions.complete_transaction(user_id)
#
#
# @users_blueprint.route('/test_stripe')
# def test_stripe():
#     transactions.test_stripe()

