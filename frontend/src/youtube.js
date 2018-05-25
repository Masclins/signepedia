const Youtube = require("youtube-api");
const opn = require("opn");
const handler = require("./handler.js");

let oauth; 

module.exports = {

    oauth2authentication(req, res) {
        oauth = Youtube.authenticate({
            type: "oauth",
            client_id: req.query.client_id,
            client_secret: req.query.client_secret,
            redirect_url:"http://signepedia.cat/oauth2callback"
        });

        opn(oauth.generateAuthUrl({
            access_type: "offline",
            scope: ["https://www.googleapis.com/auth/youtube.upload"]
        }));

        handler.index(req, res);
    },

    handleOauth2Callback(req, res) {
        oauth.getToken(req.query.code, (err, tokens) => {
            oauth.setCredentials(tokens);
        });

        handler.index(req, res);
    },

    upload(req, res){
        let form = req.body;
        let description = "Autor: " + form.author;
        Youtube.videos.insert({
            resource: {
                snippet: {
                    title: form.word,
                    description
                },
                status: {
                    privacyStatus: "unlisted",
                    license: "creativeCommon"
                }
            },
            part: "snippet,status",
            media: {
                body: req.files.video.data
            }
        }, (err, data) => {
            form.videoId = data.id;
            handler.uploadVideo(form, res);
        });
    }
};
