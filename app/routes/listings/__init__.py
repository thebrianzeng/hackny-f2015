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


@listings_blueprint.route('/<int:listing_id>/update', methods=['GET', 'POST'])
def update_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    if request.method == 'POST':
        listing.price = request.form['price']
        listing.description = request.form['description']
        listing.name = request.form['name']
        listing.email = request.form['email']

        db.session.commit()

        redirect_path = '/users/' + str(listing.user_id) + '/listings'
        return redirect(redirect_path)
    else:
        return render_template('update_listing.html', listing=listing)


@listings_blueprint.route('/<listing_id>/delete')
def delete_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    db.session.delete(listing)
    db.session.commit()
    redirect_path = '/users/' + str(listing.user_id) + '/listings'
    return redirect(redirect_path)

@listings_blueprint.route('/<listing_id>/complete')
def complete_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    listing.sold = True
    db.session.commit()
    redirect_path = '/users/' + str(listing.user_id) + '/listings'
    return redirect(redirect_path)
