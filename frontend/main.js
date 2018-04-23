var options = ["conill", "os"];

var idx = location.href.indexOf("=");
if (idx !== -1) {
    var paraula = location.href.substring(
            idx+1);

    var el = document.getElementById("resultat");
    if (options.includes(paraula)) {
        el.innerHTML = paraula + "<br>" +
            "<video width='320' height='240' controls>" +
            "<source src='../backend/videos/" + paraula + ".mp4' type='video/mp4'>" +
            "</video>";
    } else {
        el.innerHTML = 'La paraula "' + paraula + '" no la tenim registrada';
    }
}
