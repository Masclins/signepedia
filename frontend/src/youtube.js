const Youtube = require("youtube-api");
const opn = require("opn");

let oauth; 

module.exports = {
    
    oauth2authentication(req, res) {
        oauth = Youtube.authenticate({
            type: "oauth",
            client_id: req.query.client_id,
            client_secret: req.query.client_secret,
            redirect_url:"http://localhost:8080/oauth2callback"
        });

        opn(oauth.generateAuthUrl({
            access_type: "offline",
            scope: ["https://www.googleapis.com/auth/youtube.upload"]
        }));

        res.render("index", {paraula: null, video: null, alternatives: null, sinonims: null, correccio: null});
    },

    handleOauth2Callback(req, res) {
        oauth.getToken(req.query.code, (err, tokens) => {
            oauth.setCredentials(tokens);
        });
        
        res.render("index", {paraula: null, video: null, alternatives: null, sinonims: null, correccio: null});
    },

    upload(req){
        let dades = req.body;
        let descripcio = "Autor: " + dades.autor;
        if (dades.comentari !== "") {
            descripcio += ", Comentari: " + dades.comentari;
        }
        if (dades.email !== "") {
            descripcio += ", E-mail: " + dades.email;
        }
        Youtube.videos.insert({
            resource: {
                snippet: {
                    title: dades.paraula,
                    description: descripcio
                },
                status: {
                    privacyStatus: "private",
                    license: "creativeCommon"
                }
            },
            part: "snippet,status",
            media: {
                body: req.files.video.data
            }
        });
    },
};
