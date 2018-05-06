const express = require("express");
const fileUpload = require('express-fileupload');
const bodyParser = require("body-parser");
const request = require('request');
const nodemailer = require('nodemailer');
const app = express();

const obte = require('./obte_codi_html.js');

app.use(express.static("public"));
app.use(fileUpload());
app.use(bodyParser.urlencoded({extended: true}));
app.set("view engine", "ejs");

app.get('/', function(req, res) {
    res.render("index", {paraula: null, resultat: null});
});

app.get('/pujar_video', function(req, res) {
    res.render("pujar_video", {missatge: null});
});

app.post('/', function (req, res) {
    let paraula = req.body.paraula;
    let url = `http://backend:5000/diccionari/${paraula}`
    request(url, function (err, response, body) {
        let entrada = JSON.parse(body);
        res.render("index", {paraula: paraula, resultat: require('./obte_codi_html.js').html_resultat(entrada)});
    });
});

app.post('/pujar_video', function (req, res) {
    let video = req.files.video;
    
    video.mv('/video_tmp.mp4', function(err) {
        if (err) {
            return res.status(500).send(err);
        }
    });
    
    var transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'signepedia@gmail.com',
            pass: 'ensignopedia'
        }
    });
    
    var mailOptions = {
        from: 'signepedia@gmail.com',
        to: 'signepedia@gmail.com',
        subject: 'Nou vídeo: ' + req.body.paraula,
        html: 'Autor: ' + req.body.autor
              + '<br>Correu: ' + req.body.email
              + '<br>Parula: ' + req.body.paraula
              + '<br>Comentari: ' + req.body.comentari,
        attachments: [{filename: req.body.paraula + '.mp4', path: '/video_tmp.mp4'}]
    };
    
    transporter.sendMail(mailOptions, function(error, info) {
        if (error) {
            res.render("pujar_video", {missatge: "fail"});
        } else {
            res.render("pujar_video", {missatge: "exit"});
        }
    });
});

app.listen(8080, function() {
});
