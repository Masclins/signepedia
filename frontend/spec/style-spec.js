const style = require("../src/style.js");

describe("Tests for commaSplit", function () {
    it("Returns ennumeration", function () {
        expect(style.commaSplit(["un"]))
        .toBe("<button class=\"invisible\" name=\"word\" value=\"un\">\"un\"</button>.");
        expect(style.commaSplit(["a", "b", "c"]))
        .toBe("<button class=\"invisible\" name=\"word\" value=\"a\">\"a\"</button>, <button class=\"invisible\" name=\"word\" value=\"b\">\"b\"</button> o <button class=\"invisible\" name=\"word\" value=\"c\">\"c\"</button>.");
        expect(style.commaSplit(["xip", "xop"]))
        .toBe("<button class=\"invisible\" name=\"word\" value=\"xip\">\"xip\"</button> o <button class=\"invisible\" name=\"word\" value=\"xop\">\"xop\"</button>.");
    });
});
