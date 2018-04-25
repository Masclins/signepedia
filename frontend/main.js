function mostra_entrada(entrada) {
    var entrada = JSON.parse(entrada);
    
    var el = document.getElementById("resultat");
    if (entrada.url == "SenseResultat") {
        el.innerHTML = 'No tenim "' + entrada.paraula + '" registrada';
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
    if (idx !== -1) {
        return location.href.substring(idx+1); //agafa tot el que hi ha després del '='
    } else {
        return ""
    }
}

var paraula = obte_paraula();
if (paraula != "") {
    httpGetAsync(
            "http://127.0.0.1:5000/diccionari/" + paraula,
            mostra_entrada); //GET 
}

