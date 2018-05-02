const creaHTML = require("../src/creaHTML.js");

describe("Retorna codi html", function () {
    it("Hauria de retornar un <iframe>", function () {
        expect(creaHTML.creaHTML("URL", "youtube")).toBe("<iframe width='480' height='360' allow='autoplay' src='URL'></iframe>");
    });

    it("Hauria de retornar un <video>", function () {
        expect(creaHTML.creaHTML("URL2", "patata")).toBe("<video width='480' height='360' controls autoplay muted src='URL2'></video>");
    });
});
