// Returns a <button> with "invisible" class.
function invisibleButton(word) {
    return "<button class=\"invisible\" name=\"word\" value=\"" + word + "\">\"" + word + "\"</button>";
}

module.exports = {
    
    invisibleButton,

    // Returns a string enumerating the words of an array.
    commaSplit(words) {
        var r = invisibleButton(words[0]);
        if (words.length === 1) {
            return r + ".";
        } else if (words.length > 2) {
            for (var word of words.slice(1, -1)) {
                r += ", " + invisibleButton(word);
            }
        }
        r += " o " + invisibleButton(words.pop()) + ".";
        return r;
    }
};
