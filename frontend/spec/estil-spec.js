const estil = require("../src/estil.js");

describe("Tests de separaComes", function () {
    it("Hauria de retornar una enumeració", function () {
        expect(estil.separaComes(["un"]))
        .toBe("<button class=\"invisible\" name=\"paraula\" value=\"un\">\"un\"</button>.");
        expect(estil.separaComes(["a", "b", "c"]))
        .toBe("<button class=\"invisible\" name=\"paraula\" value=\"a\">\"a\"</button>, <button class=\"invisible\" name=\"paraula\" value=\"b\">\"b\"</button> o <button class=\"invisible\" name=\"paraula\" value=\"c\">\"c\"</button>.");
        expect(estil.separaComes(["xip", "xop"]))
        .toBe("<button class=\"invisible\" name=\"paraula\" value=\"xip\">\"xip\"</button> o <button class=\"invisible\" name=\"paraula\" value=\"xop\">\"xop\"</button>.");
    });
});
