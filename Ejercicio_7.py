"""
Definir una función superposicion() que tome dos listas y devuelva True
si tienen al menos 1 miembro en común o devuelva False de lo contrario.
Escribir la función usando el bucle for anidado.
"""
from shlex import join
from typing import List


def superposicion(lista_1 :List, lista_2 :List) -> bool:
    """Verifica si entre dos listas hay al menos un elemento en comun
    Args:
        lista_1 (List): Primera lista
        lista_2 (List): Segunda lista
    Returns:
        bool: True si comparten al menos un elemento, False de lo contrario
    """
    for elemento_1 in lista_1:
        for elemento_2 in lista_2:
            if(elemento_1 == elemento_2):
                return True
    return False

resultado = superposicion(['a','b','c'], ['e','f','g'])
print(resultado)
resultado_2 = superposicion(['a','b','c'], ['e','a','g'])
print(resultado_2)