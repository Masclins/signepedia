function mostra_entrada(entrada) {
    var entrada = JSON.parse(entrada);
    
    var el = document.getElementById("resultat");
    if (entrada.url === undefined) {
        el.innerHTML = 'No tenim "' + entrada.paraula + '" registrada';
        if (entrada.sinonims.length > 0) {
            el.innerHTML += "<br>Però si que tenim: ";
            el.innerHTML += entrada.sinonims[0];
            for (i = 1; i < entrada.sinonims.length; ++i) {
                el.innerHTML += ", " + entrada.sinonims[i];
            }
        }
    } else {
        if (entrada.origen == "youtube") {
            el.innerHTML = html_youtube(entrada.url);
        } else {
            el.innerHTML = html_video(entrada.url);
        }
    }
}

function obte_paraula () {
    var idx = location.href.indexOf("=");
    if (idx === -1) { return ""; }
    
    var paraula = location.href.substring(idx+1); //agafa tot el que hi ha després del '='
    return paraula.replace("+", " ");
}

var paraula = obte_paraula();
if (paraula != "") {
    httpGetAsync(
            "http://127.0.0.1:5000/diccionari/" + paraula,
            mostra_entrada); //GET 
}

