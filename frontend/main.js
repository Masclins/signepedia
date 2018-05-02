const express = require("express");
const bodyParser = require("body-parser");
const request = require('request');
const app = express();

const obte = require('./src/obte_codi_html.js');

app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended: true}));
app.set("view engine", "ejs");

app.get('/', function(req, res) {
    res.render("index", {paraula: null, resultat: null});
});

app.post('/', function (req, res) {
    let paraula = req.body.paraula;
    let url = `http://backend:5000/diccionari/${paraula}`
    request(url, function (err, response, body) {
        let entrada = JSON.parse(body);
        res.render("index", {paraula: paraula, resultat: require('./src/obte_codi_html.js').html_resultat(entrada)});
    });
});

app.listen(8080, function() {
});
