var creaHTML = require("./creaHTML.js");

    // Retorna un vector com un string enumerant els seus elements.

function separa_comes(vector) {
	r = '"' + vector[0] + '"';
	if (vector.length == 1) {
		return r+'.';
	} else if (vector.length > 2) {
		for (i = 1; i < vector.length-1; ++i) {
			r += ', "' + vector[i] + '"';
		}
	}
	r += ' o "' + vector[vector.length-1] + '".';
	return r;
}

module.exports = {

    // Comprova la informació de l'entrada que tenim i retorna el codi HTML per mostrar-la.

    html_resultat: function(entrada) {
        var resposta = "";
        if (entrada.url === undefined) {
            if (entrada.alternatives !== undefined) {
                resposta = "Quina definició t'interessa? ";
                resposta += separa_comes(entrada.alternatives);
            } else {
                resposta = 'No tenim "' + entrada.paraula + '" registrada.';
                if (entrada.sinonims !== undefined) {
                    resposta += '<br>Però sí que tenim: ';
                    resposta += separa_comes(entrada.sinonims);
                } else if (entrada.correccio !== undefined) {
                    resposta += '<br>Potser volies dir ';
                    resposta += '"' + entrada.correccio + '"?';
                }
            }
        } else {
            resposta = creaHTML.videoHTML(entrada.url, entrada.origen);
            if (entrada.alternatives !== undefined) {
                resposta += "<br>Poter t'interessa: ";
                resposta += separa_comes(entrada.alternatives);
            }
        }

        return resposta;
    }
}
