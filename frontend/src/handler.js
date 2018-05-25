const request = require("request");
const createHTML = require("./createHTML.js");

var nvideos = -1;

function renderIndex (res, entry = {}) {
    var emptyEntry = Object.keys(entry).length === 0 && entry.constructor === Object;
    res.render("index", {
        nvideos,
        word: emptyEntry ? null : entry.word,
        video: createHTML.videoHTML(entry) ,
        alternatives: createHTML.alternatives(entry),
        synonyms: createHTML.synonyms(entry),
        correction: createHTML.correction(entry)
    });
}

module.exports = {
    
    // Requests and saves the number of registered videoIds.
    getNvideos() {
        request("http://backend:5000/counter", function(err, response, rn){
            nvideos = rn;
        });
    },

    // Renders an empty main page.
    index(req, res) {
        renderIndex(res);
    },

    // Requests the search of a word.
    // Renders the main page for that search.
    search(req, res) {
        let word = req.body.word;
        let codedWord  = encodeURIComponent(word);
        let url = "http://backend:5000/dictionary/" + codedWord;
        request(url, function (err, response, body) {
            let entry = JSON.parse(body);
            renderIndex(res, entry);
        });
    },

    // Requests a video to be included into the database.
    uploadVideo(data, res) {
        request("http://backend:5000/new_entry/" + encodeURIComponent(JSON.stringify(data)), function(err, response){
            res.render("pujar_video", {message: response.body});
        });
    },

    // Requests the first unvalidated entry.
    getUnvalidated(req, res) {
        request("http://backend:5000/get_unvalidated", function(err, response){
            if (JSON.parse(response.body).error === "empty") {
                res.render("validar", {message: "empty", data: {}});
            } else {
                res.render("validar", {message: null, data: JSON.parse(response.body)});
            }
        });
    },

    // Requests an unvalidated entry to be validated.
    validate(req, res) {
        request("http://backend:5000/validate/" + encodeURIComponent(JSON.stringify(req.body)), function(err, response){
            res.render("validar", {message: response.body, data: {}});
        });
    }
};
