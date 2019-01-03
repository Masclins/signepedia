const request = require("request");

module.exports = {
	// Requests the search of a word.
	// Renders the page for that search.
	search(req, res) {
		request.get(
		"http://backend:5000/dictionary/" + encodeURIComponent(req.query.s),
		(error, response, body) => res.render("cerca", {data: JSON.stringify(JSON.parse(body))}));
	},
};
