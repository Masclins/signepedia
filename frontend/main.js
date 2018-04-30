
// Comprovem si tenim informacio de la paraula entrada. En cas
// afirmatiu, mostrem per pantalla el video corresponent.
// En cas que no en tinguem, mostrem per pantalla informacio
// relativa a la llista de sinonims de la paraula entrada.


function mostra_entrada(entrada) {
    var entrada = JSON.parse(entrada);
    
    var el = document.getElementById("resultat");
    if (entrada.url === undefined) {
        el.innerHTML = 'No tenim "' + entrada.paraula + '" registrada';
        if (entrada.sinonims.length > 0) {
            el.innerHTML += "<br>Però sí que tenim: ";
            el.innerHTML += entrada.sinonims[0];
            for (i = 1; i < entrada.sinonims.length; ++i) {
                el.innerHTML += ", " + entrada.sinonims[i];
            }
        }
    } else {
        if (entrada.origen === "youtube") {
            el.innerHTML = html_youtube(entrada.url);
        } else {
            el.innerHTML = html_video(entrada.url);
        }
    }
}

// Inspeccionem a quina posicio es troba "=". Si no apareix en cap lloc, vol dir que 
// no hi ha cap matching amb la paraula entrada. En cas que hi aparegui, agafem tot el
// que es troba a la dreta del signe "=" reemplaçant el(s) "+" per un espai.

function obte_paraula () {
    var idx = location.href.indexOf("=");
    if (idx === -1) { return ""; }
    
    var paraula = location.href.substring(idx+1); //agafa tot el que hi ha després del '='
    return paraula.replace("+", " ");
}

var paraula = obte_paraula();
if (paraula !== "") {
    httpGetAsync(
            "http://127.0.0.1:5000/diccionari/" + paraula,
            mostra_entrada); //GET 
}

