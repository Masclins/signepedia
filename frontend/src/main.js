const express = require("express");
const bodyParser = require("body-parser");
// Any REST request is handled by the handler.
const handler = require("./handler.js");
const fileUpload = require("express-fileupload");
const youtube = require("./youtube.js");
const app = express();

app.use(express.static("public"));
app.use(fileUpload());
app.use(bodyParser.urlencoded({extended: true}));
app.set("view engine", "ejs");

// Loads the sitemap for the web (for Google).
app.get("/sitemap.xml", function(req, res) {
    res.header("Content-Type", "application/xml");
    res.send(require("./sitemap.js").sitemap);
});

// GET renders main page.
app.get("/", handler.index);

// GET renders a search page
app.get("/search", handler.search);

// GET renders the edit for a page.
// POST applies changes
app.get("/edit", handler.renderEdit);
app.post("/edit", handler.applyEdit);

// GET renders uploading page.
// POST uploads a video
app.get("/upload", function(req, res) {
    res.render("upload", {message: null});
});
app.post("/upload", youtube.upload);

// GET renders validate page.
// It loads already showing the first entry to validate.
// POST validates an unvalidated entry.
app.get("/validar", handler.getUnvalidated);

// GET renders registration page.
// POST registers a new user.
app.get("/register", function(req, res) {
    res.render("register", {message: null});
});
app.post("/register", handler.newUser);

// Renders Terms of Use and Privacy Policy.
app.get("/terms", function(req, res) {
    res.render("terms");
});
app.get("/privacy", function(req, res) {
    res.render("privacy");
});


app.get("/oauth2authentication", youtube.oauth2authentication);
app.get("/oauth2callback", youtube.handleOauth2Callback);

app.listen(8080, function() {
});
