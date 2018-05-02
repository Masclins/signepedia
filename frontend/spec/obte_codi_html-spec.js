const obte = require("../src/obte_codi_html.js");

describe("Retorna el codi de l'entrada", function () {
    it("Hauria de disculpar-se", function () {
        expect(obte.html_resultat({"paraula":"fracaso_absoluto", "sinonims":[]})).toBe('No tenim "fracaso_absoluto" registrada');
    });

    it("Hauria de retornar els sinònims", function () {
        expect(obte.html_resultat({"paraula":"brunada", "sinonims":["pifia", "cagada", "lolaso"]})).toBe('No tenim "brunada" registrada<br>Però sí que tenim: "pifia", "cagada", "lolaso"');
    });

    it("Hauria de retornar un <iframe>", function () {
        expect(obte.html_resultat({"url":"link_de_youtube", "origen":"youtube"})).toBe("<iframe width='480' height='360' allow='autoplay' src='link_de_youtube'></iframe>");
    });

    it("Hauria de retornar un <video>", function () {
        expect(obte.html_resultat({"url":"link_diferent", "origen":""})).toBe("<video width='480' height='360' controls autoplay muted src='link_diferent'></video>");
    });
});
