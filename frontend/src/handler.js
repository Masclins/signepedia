const request = require("request");
const crypte = require("crypto");

module.exports = {
	// Requests the search of a word.
	// Renders the page for that search.
	search(req, res) {
		request.get(
		"http://backend:5000/dictionary/" + encodeURIComponent(req.query.s),
		(error, response, body) => res.render("cerca", {data: JSON.stringify(JSON.parse(body))}));
	},
    
    newUser(req, res) {
        if (req.body.psw !== req.body.pswRepeat) {
            res.render("register", {message: "password"});
        } else {
            let newUser = {
                "name": req.body.uname,
                "email": req.body.email,
                "password": crypto.createHash("sha1").update(req.body.psw).digest("hex")
            };
            request.post(
                    "http://localhost:5000/users/" + encodeURIComponent(JSON.stringify(newUser)),
                    (error, response) => res.render("register", {message: response.body}));
        }
    },
};
