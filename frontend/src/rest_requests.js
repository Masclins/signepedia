const request = require("request");
const nodemailer = require("nodemailer");
const creaHTML = require("./creaHTML.js");
const fs = require("fs");

module.exports = {
    
    // Cerca una paraula a partir d'una REST request.
    
    cerca(req, res) {
        let paraula = req.body.paraula;
        let paraulaCodificada  = encodeURIComponent(paraula);
        let url = `http://backend:5000/diccionari/${paraulaCodificada}`;
        request(url, function (err, response, body) {
            let entrada = JSON.parse(body);
            res.render("index", {
                            paraula: entrada.paraula, 
                            video: creaHTML.videoHTML(entrada),
                            alternatives: creaHTML.alternatives(entrada),
                            sinonims: creaHTML.sinonims(entrada),
                            correccio: creaHTML.correccio(entrada)
                        });
        });
    },
    
    // Puja un video a partir d'una REST request.
    
    pujaVideo(req, res) {
        let video = req.files.video;
        
        video.mv("/video_tmp.mp4", function(err) {
            if (err) {
                return res.status(500).send(err);
            }
        });
        
        fs.readFile("./dades_correu.json", "utf8", function (err, data) {
            if (err) {
                res.render("pujar_video", {missatge: "fail"});
            } else {
                let dadesCorreu = JSON.parse(data);
                let transporter = nodemailer.createTransport({
                    service: "gmail",
                    auth: {
                        user: dadesCorreu.usuari,
                        pass: dadesCorreu.contrasenya
                    }
                });
                
                let mailOptions = {
                    from: dadesCorreu.usuari,
                    to: "signepedia@gmail.com",
                    subject: "Nou video: " + req.body.paraula,
                    html: "Autor: " + req.body.autor
                        + "<br>Correu: " + req.body.email
                        + "<br>Parula: " + req.body.paraula
                        + "<br>Comentari: " + req.body.comentari
                        + "<br><br>Qui ha enviat aquest vídeo confirma que és l'autor del vídeo, l'únic que hi surt i té 18 anys o més."
                        + "<br> També, ha acceptat les Condicions d'ús i Política de privadesa adjuntes en aquest correu.",
                    attachments: [{filename: req.body.paraula + ".mp4", path: "/video_tmp.mp4"},
                        {filename: "Condicions d'ús", path: "/views/termes.ejs"},
                        {filename: "Política de privadesa", path: "/views/privadesa.ejs"}]
                };
                
                transporter.sendMail(mailOptions, function(error) {
                    if (error) {
                        res.render("pujar_video", {missatge: "fail"});
                    } else {
                        res.render("pujar_video", {missatge: "exit"});
                    }
                });
            }
        });
    }
};
