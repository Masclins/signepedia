const sm = require("sitemap");

module.exports = {
    sitemap: sm.createSitemap({
        hostname: "http://signepedia.cat",
        cacheTime: 60000,
        urls: [
            {url: "/", priority: 1},
            {url: "/comunitat", priority: 0.6},
            {url: "/privadesa", priority: 0.1},
            {url: "/condicions", priority: 0.1}
        ]}).toString()
};
