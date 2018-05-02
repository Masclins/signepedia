var creaHTML = require("./creaHTML.js");

module.exports = {

    // Comprovem si tenim informació de la paraula entrada.
    // En cas afirmatiu, retornem el codi HTML per mostrar
    // el video corresponent. En cas que no en tinguem,
    // retornem el codi HTML per mostrar els sinònims que
    // tenim de la paraula entrada.

    html_resultat: function(entrada) {
        var resposta = "";
        if (entrada.url === undefined) {
            resposta = 'No tenim "' + entrada.paraula + '" registrada';
            if (entrada.sinonims.length > 0) {
                resposta += "<br>Però sí que tenim: ";
                resposta += entrada.sinonims[0];
                for (i = 1; i < entrada.sinonims.length; ++i) {
                    resposta += ", " + entrada.sinonims[i];
                }
            }
        } else {
            resposta = creaHTML.creaHTML(entrada.url, entrada.origen);
        }

        return resposta;
    }
}
