const estil = require("./estil.js");
const width = 480;
const height = 360;

function creaForm(str) {
    return "<form action='/' method='post'>" + str + "</form>";
}

module.exports = {

    // Retorna el codi HTML per mostrar un vídeo.
    // Si l'"origen" és youtube, retorna un <iframe>.
    // Altrament, retorna un <video>.

    videoHTML(entrada) {
        if (entrada.url == null) {
            if (entrada.paraula == null) {
                return null;
            } else {
                return "Ho sentim, no tenim \"" + entrada.paraula + "\" registrada.";
            }
        } else if (entrada.origen === "youtube") {
            return "<iframe width='" + width + "' height='" + height + "' allow='autoplay' src='" + entrada.url + "?&autoplay=1&mute=1&rel=0&showinfo=0'></iframe>";
        } else {
            return "<video width='" + width + "' height='" + height + "' controls autoplay muted src='" + entrada.url + "'></video><br><p class='autor'>Autor/a del vídeo: " + entrada.autor + ".</p>";
        }
    },

    // Retorna les alternatives, sinonims o correccio.
    // Els converteix en una <form> per fer que cada paraula sigui un <button>.
    // D'aquesta manera al apretar-los es pot fer un POST request.
    
    alternatives(entrada) {
        if (entrada.alternatives == null) {
            return null;
        } else {
            return creaForm("Potser t'interessa: " + estil.separaComes(entrada.alternatives));
        }
    },

    sinonims(entrada) {
        if (entrada.sinonims == null) {
            return null;
        } else {
            return creaForm("Pots cercar els sinònims: " + estil.separaComes(entrada.sinonims));
        }
    },

    correccio(entrada) {
        if (entrada.correccio == null) {
            return null;
        } else {
            return creaForm("Potser volies dir " + estil.botoInvisible(entrada.correccio) + "?");
        }
    }
};
