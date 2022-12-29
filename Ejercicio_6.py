"""
Definir una función es_palindromo() que reconoce palíndromos
(es decir, palabras que tienen el mismo aspecto escritas invertidas),
Ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def comparar(a :bool,b :bool) -> bool:
    if(a ==b ):
        return True
    else:
        return False

def es_palindromo(palabra :str) -> bool:
    """Verifica si una cadena es palindromo
    Args:
        palabra (str): cadena que sera analizada
    Returns:
        bool: True si es palindromo, False de lo contrario
    """
    ultimo = len(palabra)-1
    for numero in range(0,len(palabra)):
        if (comparar(palabra[numero],palabra[ultimo])):
            ultimo = ultimo -1
        else: return False
    return True

resultado = es_palindromo('ana')
print(resultado)
resultado_2 = es_palindromo('nana')
print(resultado_2)