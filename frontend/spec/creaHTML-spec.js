const creaHTML = require("../src/creaHTML.js");

describe("Tests de videoHTML", function () {
    it("Hauria de retornar un <iframe>", function () {
        expect(creaHTML.videoHTML({"videoId":"c0dI", "qualsevol": "valor"}))
        .toBe("<iframe width=\"480\" height=\"360\" allow=\"autoplay\" src=\"https://www.youtube.com/embed/c0dI?&autoplay=1&mute=1&rel=0&showinfo=0\"></iframe>");
    });

    it("Hauria de disculpar-se", function () {
        expect(creaHTML.videoHTML({"paraula": "missigno", "attr": "val"}))
        .toBe("Ho sentim, no tenim \"missigno\" registrada.");
    });

    it("Hauria de retornar null", function () {
        expect(creaHTML.videoHTML({}))
        .toBe(null);
    });
});

describe("Tests d'alternatives", function () {

    it("Retorna null quan hauria", function () {
        expect(creaHTML.alternatives({"alternatives": ["pim", "pam", "pum"]}))
        .not.toBe(null);
        expect(creaHTML.alternatives({"alternatives": ["blanc", "negre"], "paraula": "color"}))
        .not.toBe(null);
        expect(creaHTML.alternatives({}))
        .toBe(null);
    });
});

describe("Tests de sinonims", function () {

    it("Retorna null quan hauria", function () {
        expect(creaHTML.sinonims({"paraula": "brunada", "sinonims": ["pifia", "cagada"]}))
        .not.toBe(null);
        expect(creaHTML.sinonims({"paraula": "únic", "alternatives": ["cap", "ni", "una"], "correccio": "bonic"}))
        .toBe(null);
    });
});

describe("Tests de correccio", function () {

    it("Retorna null quan hauria", function () {
        expect(creaHTML.correccio({"paraula": "tatatania", "correccio": "Tània"}))
        .not.toBe(null);
        expect(creaHTML.correccio({"paraula": "correctíssim"}))
        .toBe(null);
    });
});
