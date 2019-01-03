const express = require("express");
const bodyParser = require("body-parser");
// Any REST request is handled by the handler.
const handler = require("./handler.js");
const fileUpload = require("express-fileupload");
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

// Renders all pages.
app.get("/", function(req, res) {
    res.render("index");
});
app.get("/comunitat", function(req, res) {
    res.render("comunitat");
});
/*app.get("/diccionari", function(req, res) {
    res.render("diccionari");
});
app.get("/registre", function(req, res) {
    res.render("registre");
});*/
app.get("/condicions", function(req, res) {
    res.render("condicions");
});
app.get("/privadesa", function(req, res) {
    res.render("privadesa");
});

app.get("/cerca", handler.search);

app.listen(8080, function() {
});
