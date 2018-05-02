module.exports = {

    // Agafem com a paràmetre una url en formatt string i
    // retornem el codi HTML necessàri per mostrar-lo.
    // iframe: document HTML integrat dins d'un altre,
    // en aquest cas agafem un vídeo que es troba dins
    // d'un altre document HTML.

    creaHTML: function(url, origen) {
        if (origen === "youtube") {
            return "<iframe width='480' height='360' allow='autoplay' src='" + url + "'></iframe>";
        } else {
            return "<video width='480' height='360' controls autoplay muted src='" + url + "'></video>";
        }
    }
}
