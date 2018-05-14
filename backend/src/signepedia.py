from src import cercador
from src import sinonims
from src import corrector

# Eliminem les paraules dels "sinonims" que ja son a "alternatives"

def neteja_entrada(entrada):
    if not "alternatives" in entrada or not "sinonims" in entrada:
        return entrada
    for s in entrada["sinonims"]:
        if s in entrada["alternatives"]:
            entrada["sinonims"].remove(s)
    if not entrada["sinonims"]:
        del entrada["sinonims"]
    return entrada

# Cerquem tota la informació que volem passar al frontend d'una paraula.
# Creem una entrada on passem el que tenim:
# 1- Entrada de "paraula"
# 2- Alternatives de "paraula"
# 3- Sinònims de "paraula"
# 4- (Si 1, 2 i 3 fallen) Correcció ortogràfica de "paraula"

def retorna_entrada(paraula):
    entrada = cercador.obte_entrada(paraula)
    alternatives = sinonims.troba_sinonims(paraula)
    if entrada is None and alternatives is not None:
        return dict(paraula=paraula, sinonims=alternatives)
    elif entrada is not None:
        if alternatives is not None:
            entrada["sinonims"] = alternatives
        return neteja_entrada(entrada)
    return corrector.corregeix_paraula(paraula)
