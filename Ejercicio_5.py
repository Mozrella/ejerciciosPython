"""
Definir una función inversa() que calcule la inversión de una cadena.
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(cadena : str) -> str:
    """Dado una cadena, calcula la inversa de la misma
    Args:
        cadena (str): cadena que sera invertida
    Returns:
        str: cadena invertida
    """
    largo= len(cadena) - 1
    nueva_cadena = ''
    nuevo_indice =0
    for numero in range(0,len(cadena)):
        nueva_cadena= nueva_cadena+cadena[largo]
        largo = largo - 1
    return nueva_cadena

resultado = inversa('Reversa')
print(resultado)