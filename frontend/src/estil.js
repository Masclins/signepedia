module.exports = {

    // Retorna un vector com un string enumerant els seus elements.
    separa_comes: function(vector) {
        r = '"' + vector[0] + '"';
        if (vector.length == 1) {
    	    return r+'.';
        } else if (vector.length > 2) {
    	for (i = 1; i < vector.length-1; ++i) {
    	        r += ', "' + vector[i] + '"';
	    }
        }
        r += ' o "' + vector[vector.length-1] + '".';
        return r;
    }
}
