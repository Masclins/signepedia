const estil = require('./estil.js');
const width = 480;
const height = 360;

module.exports = {

    // Retorna el codi HTML per mostrar un vídeo.
    // Si l'"origen" és youtube, retorna un <iframe>.
    // Altrament, retorna un <video>.

    videoHTML: function(entrada) {
        if (entrada.url === undefined) {
            if (entrada.paraula === undefined) {
                return null;
            } else {
                return 'Ho sentim, no tenim "' + entrada.paraula + '" registrada.';
            }
        } else if (entrada.origen === "youtube") {
            return "<iframe width='" + width + "' height='" + height + "' allow='autoplay' src='" + entrada.url + "?&autoplay=1&mute=1&rel=0&showinfo=0'></iframe>";
        } else {
            return "<video width='" + width + "' height='" + height + "' controls autoplay muted src='" + entrada.url + "'></video>";
        }
    },

    alternatives: function(entrada) {
        if (entrada.alternatives == undefined) {
            return null;
        } else {
            return "Potser t'interessa: " + estil.separa_comes(entrada.alternatives);
        }
    },

    sinonims: function(entrada) {
        if (entrada.sinonims === undefined) {
            return null;
        } else {
            return "Pots cercar els sinònims: " + estil.separa_comes(entrada.sinonims);
        }
    },

    correccio: function(entrada) {
        if (entrada.correccio === undefined) {
            return null;
        } else {
            return 'Potser volies dir "' + entrada.correccio + '"?';
        }
    }
}
