const express = require("express");
const bodyParser = require("body-parser");
const rest_requests = require("./rest_requests.js");
const fileUpload = require('express-fileupload');
const app = express();

app.use(express.static("public"));
app.use(fileUpload());
app.use(bodyParser.urlencoded({extended: true}));
app.set("view engine", "ejs");

// Carreguem la pàgina principal, amb totes les variables null
app.get('/', function(req, res) {
    res.render("index", {paraula: null, video: null, alternatives: null, sinonims: null, correccio: null});
});

// Carreguem la pàgina principal, sense cap missatge
app.get('/pujar_video', function(req, res) {
    res.render("pujar_video", {missatge: null});
});

// Rebem una petició POST. Les gestiona rest_requests.
app.post('/', rest_requests.cerca);

app.post('/pujar_video', rest_requests.puja_video);

app.listen(8080, function() {
});
