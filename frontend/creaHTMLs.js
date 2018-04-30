
//  Agafem com a parametre una url en format string i retornem directament 
//  l'arxiu que tenen integrat(embedded). En aquest cas es un arxiu de video i iframe.
//  iframe: document HTML integrat dins d'un altre. En aquest cas, agafem un video 
//  que es troba dins d'un altre document HTML.

function html_video(url) {
    return "<video width='320' height='240' controls autoplay muted src='" + url + "'></video>";
}

function html_youtube(url) {
    return "<iframe width='320' height='240' allow='autoplay' src='" + url + "'></iframe>";
}
