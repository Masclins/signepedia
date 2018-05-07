const creaHTML = require("../src/creaHTML.js");

describe("Tests de videoHTML", function () {
    it("Hauria de retornar un <iframe>", function () {
        expect(creaHTML.videoHTML({"url":"URL", "origen": "youtube"}))
        .toBe("<iframe width='480' height='360' allow='autoplay' src='URL?&autoplay=1&mute=1&rel=0&showinfo=0'></iframe>");
    });

    it("Hauria de retornar un <video>", function () {
        expect(creaHTML.videoHTML({"url": "URL2", "origen": "patata"}))
        .toBe("<video width='480' height='360' controls autoplay muted src='URL2'></video>");
    });

    it("Hauria de disculpar-se", function () {
        expect(creaHTML.videoHTML({"paraula": "missigno", "attr": "val"}))
        .toBe('Ho sentim, no tenim "missigno" registrada.');
    });

    it("Hauria de retornar null", function () {
        expect(creaHTML.videoHTML({}))
        .toBe(null);
    });
});

describe("Tests d'alternatives", function () {
    it("Hauria d'enumerar alternatives", function () {
        expect(creaHTML.alternatives({"alternatives": ["pim", "pam", "pum"]}))
        .toBe('Potser t\'interessa: "pim", "pam" o "pum".');
        expect(creaHTML.alternatives({"alternatives": ["aquesta i prou"], "atribut-molest": "àcçént"}))
        .toBe('Potser t\'interessa: "aquesta i prou".');
        expect(creaHTML.alternatives({"url": "link", "alternatives": ["blanc", "negre"]}))
        .toBe('Potser t\'interessa: "blanc" o "negre".');
    });

    it("Hauria de retornar null", function () {
        expect(creaHTML.alternatives({}))
        .toBe(null);
    });
});

describe("Tests de sinonims", function () {
    it("Hauria d'enumerar sinònims", function () {
        expect(creaHTML.sinonims({"sinonims": ["brunada","pifia","ridícul"]}))
        .toBe('Pots cercar els sinònims: "brunada", "pifia" o "ridícul".');
        expect(creaHTML.sinonims({"sinonims": ["miñó de terrassa"], "paraula": "castelleret"}))
        .toBe('Pots cercar els sinònims: "miñó de terrassa".');
    });

    it("Hauria de retornar null", function () {
        expect(creaHTML.sinonims({"paraula": "únic", "alternatives": ["cap", "ni", "una"], "correccio": "bonic"}))
        .toBe(null);
    });
});

describe("Tests de correccio", function () {
    it("Hauria de proposar la correcció", function () {
        expect(creaHTML.correccio({"correccio": "ortografia"}))
        .toBe('Potser volies dir "ortografia"?');
        expect(creaHTML.correccio({"correccio": "çurprënê'nt", "paraula": "sorprenent", "nota": "hagués jurat que estava ben escrita"}))
        .toBe('Potser volies dir "çurprënê\'nt"?');
    });

    it("Hauria de retornar null", function () {
        expect(creaHTML.correccio({"paraula": "correctíssim"}))
        .toBe(null);
    });
});
