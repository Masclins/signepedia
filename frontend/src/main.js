const express = require("express");
const bodyParser = require("body-parser");
const restRequests = require("./rest_requests.js");
const fileUpload = require("express-fileupload");
const fs = require("fs");
const app = express();

app.use(express.static("public"));
app.use(fileUpload());
app.use(bodyParser.urlencoded({extended: true}));
app.set("view engine", "ejs");

// Carreguem el sitemap de la pàgina
app.get("/sitemap.xml", function(req, res) {
    res.header("Content-Type", "application/xml");
    res.send(require("./sitemap.js").sitemap);
});

// Carreguem la pàgina principal, amb totes les variables null
app.get("/", function(req, res) {
    res.render("index", {paraula: null, video: null, alternatives: null, sinonims: null, correccio: null});
});

// Carreguem la pàgina principal, sense cap missatge
app.get("/pujar_video", function(req, res) {
    fs.access("./dades_correu.json", (err) => {
        if (err) {
            res.render("pujar_video", {missatge: "inhabilitat"});
        } else {
            res.render("pujar_video", {missatge: null});
        }
    });
});

// Carreguem les pàgines de Condicions d'ús o Política de privadesa
app.get("/termes", function(req, res) {
    res.render("termes");
});
app.get("/privadesa", function(req, res) {
    res.render("privadesa");
});


// Rebem una petició POST. Les gestiona restRequests.
app.post("/", restRequests.cerca);

app.post("/pujar_video", restRequests.pujaVideo);

app.listen(8080, function() {
});
