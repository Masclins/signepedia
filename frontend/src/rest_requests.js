const request = require("request");
const nodemailer = require("nodemailer");
const creaHTML = require("./creaHTML.js");
const fs = require("fs");

var dadesCorreu;

module.exports = {
	
	// Cerca una paraula a partir d'una REST request.
	
	cerca(req, res) {
		let paraula = req.body.paraula;
		let url = `http://backend:5000/diccionari/${paraula}`;
		request(url, function (err, response, body) {
			let entrada = JSON.parse(body);
			res.render("index", {
                            paraula,
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
				dadesCorreu = JSON.parse(data);
				var transporter = nodemailer.createTransport({
					service: "gmail",
					auth: {
						user: dadesCorreu.usuari,
						pass: dadesCorreu.contrasenya
					}
				});
				
				var mailOptions = {
					from: dadesCorreu.usuari,
					to: "signepedia@gmail.com",
					subject: "Nou video: " + req.body.paraula,
					html: "Autor: " + req.body.autor
                                            + "<br>Correu: " + req.body.email
                                            + "<br>Parula: " + req.body.paraula
                                            + "<br>Comentari: " + req.body.comentari,
					attachments: [{filename: req.body.paraula + ".mp4", path: "/video_tmp.mp4"}]
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
