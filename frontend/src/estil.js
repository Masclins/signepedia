
// Converteix una paraula en un botó invisible.
// Que sigui invisible depen del CSS de la "class".
function botoInvisible(paraula) {
    return "<button class=\"invisible\" name=\"paraula\" value=\"" + paraula + "\">\"" + paraula + "\"</button>";
}

module.exports = {
    
    botoInvisible,

    // Retorna un vector de paraules com un string enumerant els seus elements.
    separaComes(paraules) {
        var r = botoInvisible(paraules[0]);
        if (paraules.length === 1) {
            return r + ".";
        } else if (paraules.length > 2) {
            for (var paraula of paraules.slice(1, -1)) {
                r += ", " + botoInvisible(paraula);
            }
        }
        r += " o " + botoInvisible(paraules.pop()) + ".";
        return r;
    }
};
