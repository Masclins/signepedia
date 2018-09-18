const request = require("request");
const crypto = require("crypto");

function passJSON(JSONstr) {
    return JSON.stringify(JSON.parse(JSONstr));
}

module.exports = {
    
    // Renders an empty main page.
    index(req, res) {
        request.get(
                "http://localhost:5000/main",
                (error, response, body) => res.render("index", {data: passJSON(body), user: null}));
    },

    // Requests the search of a word.
    // Renders the main page for that search.
    search(req, res) {
        request.get(
                "http://localhost:5000/dictionary/" + encodeURIComponent(req.query.word),
                (error, response, body) => res.render("index", {data: passJSON(body), user: null}));
    },

    // Renders the edition menu for an entry
    renderEdit(req, res) {
        request.get(
                "http://localhost:5000/entries/" + req.query.id,
                (error, response, body) => res.render("edit", {entry: passJSON(body), user: null}));
    },

    // Applies an edition.
    // Returns to the search for that entry.
    applyEdit(req, res) {
        let edits = JSON.stringify({
            "word": req.body.word,
            "comment": req.body.comment,
            "video": req.body.video});
        request.patch(
                "http://localhost:5000/entries/" + req.body.id
                + "/edits/" + edits,
                (error) => request.get(
                    "http://localhost:5000/dictionary/" + encodeURIComponent(req.body.word),
                    (error, response, body) => res.render("index", {data: passJSON(body), user: null})));
    },

    // Requests a video to be included into the database.
    uploadVideo(data, res) {
        request.post(
                "http://backend:5000/dictionary/" + encodeURIComponent(JSON.stringify(data)),
                (error) => res.render("upload", {message: "done", user: null}));
    },

    // Requests the first unvalidated entry.
    getUnvalidated(req, res) {
        request("http://backend:5000/get_unvalidated", function(err, response){
            if (JSON.parse(response.body).error === "empty") {
                res.render("validate", {message: "empty", data: {}, user: null});
            } else {
                res.render("validate", {message: null, data: JSON.parse(response.body), user: null});
            }
        });
    },

    // Requests a user registration.
    newUser(req, res) {
        if (req.body.password !== req.body.passwordConf) {
            res.render("register", {message: "password"});
        } else {
            let newUser = {
                "name": req.body.name,
                "email": req.body.email,
                "password": crypto.createHash("sha1").update(req.body.password).digest("hex"),
                "birthday": req.body.birthday
            };
            request.post(
                    "http://localhost:5000/users/" + encodeURIComponent(JSON.stringify(newUser)),
                    (error, response) => res.render("register", {message: response.body}));
        }
    }
};
