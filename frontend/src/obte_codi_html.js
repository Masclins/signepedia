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
            if (entrada.alternatives !== undefined) {
                resposta = "Quina definició t'interessa? ";
                resposta += '"' + entrada.paraula + ' ' + entrada.alternatives[0] + '"';
                for (i = 1; i < entrada.alternatives.length; ++i) {
                    resposta += ', "' + entrada.paraula + ' ' + entrada.alternatives[i] + '"';
                }
            } else {
                resposta = 'No tenim "' + entrada.paraula + '" registrada';
                if (entrada.sinonims !== undefined) {
                    resposta += '<br>Però sí que tenim: ';
                    resposta += '"' + entrada.sinonims[0] + '"';
                    for (i = 1; i < entrada.sinonims.length; ++i) {
                        resposta += ', "' + entrada.sinonims[i] + '"';
                    }
                } else if (entrada.correccio !== undefined) {
                    resposta += '<br>Potser volies dir ';
                    resposta += '"' + entrada.correccio + '"?';
                }
            }
        } else {
            resposta = creaHTML.creaHTML(entrada.url, entrada.origen);
            if (entrada.alternatives !== undefined) {
                resposta += "<br>Poter t'interessa: ";
                resposta += '"' + entrada.paraula + ' ' + entrada.alternatives[0] + '"';
                for (i = 1; i < entrada.sinonims.length; ++i) {
                    resposta += ',"' + entrada.paraula + ' ' + entrada.alternatives[i] + '"';
                }
            }
        }

        return resposta;
    }
}
