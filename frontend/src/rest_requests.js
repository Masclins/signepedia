const request = require("request");
const creaHTML = require("./creaHTML.js");
const youtube = require("./youtube.js");

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
        youtube.upload(req);
        res.render("pujar_video", {missatge: "exit"});
    }
};