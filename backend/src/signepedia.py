from src import cercador
from src import sinonims
from src import corrector

# Cerquem tota la informació que volem passar al frontend d'una paraula.
# Creem una entrada on passem el que tenim, per ordre de prioritat:
# 1- Entrada de "paraula" (+ alternatives, si n'hi ha)
# 2- Alternatives de "paraula"
# 3- Sinònims de "paraula"
# 4- Correcció ortogràfica de "paraula"

def retorna_entrada(paraula):
    entrada = cercador.obte_entrada(paraula.lower())
    if entrada != None:
        return entrada
    alternativa = sinonims.troba_sinonims(paraula.lower())
    if "sinonims" in alternativa:
        return alternativa
    return corrector.corregeix_paraula(paraula.lower())       
