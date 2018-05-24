const createHTML = require("../src/createHTML.js");

describe("Tests for videoHTML", function () {
    it("Returns iframe", function () {
        expect(createHTML.videoHTML({"videoId":"c0dI", "any": "value"}))
        .toBe("<iframe width=\"480\" height=\"360\" allow=\"autoplay\" src=\"https://www.youtube.com/embed/c0dI?&autoplay=1&mute=1&rel=0&showinfo=0\"></iframe>");
    });

    it("Apologizes", function () {
        expect(createHTML.videoHTML({"word": "missigno", "attr": "val"}))
        .toBe("Ho sentim, no tenim \"missigno\" registrada.");
    });

    it("Returns null", function () {
        expect(createHTML.videoHTML({}))
        .toBe(null);
    });
});

describe("Tests for alternatives", function () {

    it("Returns null", function () {
        expect(createHTML.alternatives({"alternatives": ["pim", "pam", "pum"]}))
        .not.toBe(null);
        expect(createHTML.alternatives({"alternatives": ["blanc", "negre"], "paraula": "color"}))
        .not.toBe(null);
        expect(createHTML.alternatives({}))
        .toBe(null);
    });
});

describe("Tests for synonyms", function () {

    it("Returns null", function () {
        expect(createHTML.synonyms({"word": "brunada", "synonyms": ["pifia", "cagada"]}))
        .not.toBe(null);
        expect(createHTML.synonyms({"word": "únic", "alternatives": ["cap", "ni", "una"], "correccio": "bonic"}))
        .toBe(null);
    });
});

describe("Tests for correction", function () {

    it("Returns null", function () {
        expect(createHTML.correction({"word": "tatatania", "correction": "Tània"}))
        .not.toBe(null);
        expect(createHTML.correction({"word": "correctíssim"}))
        .toBe(null);
    });
});
