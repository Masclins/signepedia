function retorna(url) {
    var el = document.getElementById("resultat");
    if (url == "SenseResultat") {
        el.innerHTML = "No la tenim registrada";
    } else {
        el.innerHTML =
            "<video width='320' height='240' controls>" +
            "<source src='" + url + "' type='video/mp4'>" +
            "</video>";
    }
}

var idx = location.href.indexOf("=");
if (idx !== -1) {
    var paraula = location.href.substring(idx+1); //agafa tot el que hi ha després del '='
    httpGetAsync(
            "http://127.0.0.1:5000/diccionari/" + paraula,
            retorna); //GET 
}

