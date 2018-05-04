const obte = require("../src/obte_codi_html.js");

describe("Tests de html_resultat", function () {
    it("Hauria de disculpar-se", function () {
        expect(obte.html_resultat({"paraula":"fracaso_absoluto"})).toBe('No tenim "fracaso_absoluto" registrada.');
    });

    it("Hauria de retornar els sinònims", function () {
        expect(obte.html_resultat({"paraula":"Jack Sparrow", "sinonims":["pirata"]})).toBe('No tenim "Jack Sparrow" registrada.<br>Però sí que tenim: "pirata".');
        expect(obte.html_resultat({"paraula":"brunada", "sinonims":["pifia", "cagada", "lolaso"]})).toBe('No tenim "brunada" registrada.<br>Però sí que tenim: "pifia", "cagada" o "lolaso".');
    });

    it("Hauria de retornar una correcció", function () {
        expect(obte.html_resultat({"paraula":"tatatània", "correccio":"tània"})).toBe('No tenim "tatatània" registrada.<br>Potser volies dir "tània"?');
    });

    it("Hauria de retornar un <iframe>", function () {
        expect(obte.html_resultat({"url":"link_de_youtube", "origen":"youtube"})).toBe("<iframe width='480' height='360' allow='autoplay' src='link_de_youtube'></iframe>");
    });

    it("Hauria de retornar un <video>", function () {
        expect(obte.html_resultat({"url":"link_diferent", "origen":""})).toBe("<video width='480' height='360' controls autoplay muted src='link_diferent'></video>");
    });
});
