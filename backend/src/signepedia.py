from src import cercador
from src import sinonims
from src import corrector

# Convertim la paraula entrada a minuscules per evitar errors de matching
# i retornem la paraula entrada. En cas que no estigui registrada, 
# retornem una llista de sinonims.

def retorna_entrada(paraula):
    entrada = cercador.obte_entrada(paraula.lower())
    if entrada != None:
        return entrada
    else:
        alternativa = sinonims.troba_sinonims(paraula.lower())
        if "sinonims" in alternativa:
            return alternativa
        else:
            return corrector.corregeix_paraula(paraula.lower())
           
