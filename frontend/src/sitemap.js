const sm = require("sitemap");

module.exports = {
    sitemap: sm.createSitemap({
        hostname: "http://signepedia.cat",
        cacheTime: 60000,
        urls: [
            {url: "/", priority: 1},
            {url: "/pujar_video", priority: 0.8},
            {url: "/termes", priority: 0.5},
            {url: "/privadesa", priority: 0.5}
        ]}).toString()
};
