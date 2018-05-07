const estil = require('../src/estil.js');

describe("Tests de separa_comes", function () {
    it("Hauria de retornar una enumeració", function () {
        expect(estil.separa_comes(["un"]))
        .toBe('"un".');
        expect(estil.separa_comes(["a", "b", "c"]))
        .toBe('"a", "b" o "c".');
        expect(estil.separa_comes(["xip", "xop"]))
        .toBe('"xip" o "xop".');
    });
});
