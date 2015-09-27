var Listing = React.createClass({
	render: function() {
		return (
			<div className="listing" class="listing">
				<h2 className="listingName">
				{this.props.name}
				</h2>
				<div className="listingPrice">
				${this.props.price}
				</div>
				<div className="listingDescription">
				Description: {this.props.description}
				</div>
				<div className="listingEmail">
				Contact: {this.props.email}
				</div>
				<hr></hr>
			</div>
			);
	}
});

var ListingList = React.createClass({
	getInitialState: function() {
		return {data: []};
	},
	componentDidMount: function() {
		$.ajax({
			url: this.props.url,
			dataType: 'json',
			cache: false,
			success: function(data) {
				this.setState({data: data["listings"]});
			}.bind(this),
			error: function(xhr, status, err) {
				console.error(this.props.url, status, err.toString());
			}.bind(this)
		});
	},
	render: function() {
		var listingNodes = this.state.data.map(function (listing) {
			return (
				<Listing 
				name={listing.name} 
				description={listing.description}
				price={listing.price} 
				email={listing.email} />
				);
		});
		return (
			<div className="listingList">
				{listingNodes}
			</div>
			);
	}
});

React.render(
	<ListingList url="/listings/" />,
	document.getElementById('content')
	);

