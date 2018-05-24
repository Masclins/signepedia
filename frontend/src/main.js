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

handler.getNvideos();

// Loads the sitemap for the web (for Google).
app.get("/sitemap.xml", function(req, res) {
    res.header("Content-Type", "application/xml");
    res.send(require("./sitemap.js").sitemap);
});

// Renders main page.
app.get("/", handler.index);

// Renders uploading page.
app.get("/pujar_video", function(req, res) {
    res.render("pujar_video", {message: null});
});

// Renders validate page.
// It loads already showing the first entry to validate.
app.get("/validar", handler.getUnvalidated);

// Renders Terms of Use and Privacy Policy.
app.get("/termes", function(req, res) {
    res.render("termes");
});
app.get("/privadesa", function(req, res) {
    res.render("privadesa");
});


// Renders main page after a search.
app.post("/", handler.search);

// A video is uploaded.
app.post("/pujar_video", youtube.upload);

// Validate an unvalidated entry.
app.post("/validar", handler.validate);

app.get("/oauth2authentication", youtube.oauth2authentication);
app.get("/oauth2callback", youtube.handleOauth2Callback);

app.listen(8080, function() {
});
