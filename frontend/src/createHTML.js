const style = require("./style.js");
const width = 480;
const height = 360;

function createForm(str) {
    return "<form action=\"/\" method=\"post\">" + str + "</form>";
}

module.exports = {

    // Returns needed HTML code to show a YouTube video.
    // It is an <iframe>.
    videoHTML(entry) {
        if (entry.videoId == null) {
            if (entry.word == null) {
                return null;
            } else {
                return "Ho sentim, no tenim \"" + entry.word + "\" registrada.";
            }
        } else {
            return "<iframe width=\"" + width + "\" height=\"" + height + "\" allow=\"autoplay\" src=\"https://www.youtube.com/embed/" + entry.videoId + "?&autoplay=1&mute=1&rel=0&showinfo=0\"></iframe>";
        }
    },

    // Returns alternatives, synonyms or correction.
    // Everything as a <form>, so every word is a <button>.
    // This way a POST request can be done upon clicking.
    alternatives(entry) {
        if (entry.alternatives == null) {
            return null;
        } else {
            return createForm("Potser t'interessa: " + style.commaSplit(entry.alternatives));
        }
    },
    synonyms(entry) {
        if (entry.synonyms == null) {
            return null;
        } else {
            return createForm("Pots cercar els sinònims: " + style.commaSplit(entry.synonyms));
        }
    },
    correction(entry) {
        if (entry.correction == null) {
            return null;
        } else {
            return createForm("Potser volies dir " + style.invisibleButton(entry.correction) + "?");
        }
    }
};
