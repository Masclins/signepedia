module.exports = {

    // Retorna el codi HTML per mostrar un vídeo.
    // Si l'"origen" és youtube, retorna un <iframe>.
    // Altrament, retorna un <video>.

    videoHTML: function(url, origen) {
        if (origen === "youtube") {
            return "<iframe width='480' height='360' allow='autoplay' src='" + url + "'></iframe>";
        } else {
            return "<video width='480' height='360' controls autoplay muted src='" + url + "'></video>";
        }
    }
}
