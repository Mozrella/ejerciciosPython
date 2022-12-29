""""
Definir una función generar_n_caracteres() que tome un entero n
y devuelva el caracter multiplicado por n.
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n :int, elemento :str) -> str:
    """Retorna n veces un elemento enviado
    Args:
        n (int): numero de veces que el elemento sera repetido
        elemento (str): elemento que debera repetise
    Returns:
        str: Cadena con el elemento repetido n veces
    """
    nueva_cadena = ''
    for numero in range(0, n):
        nueva_cadena = nueva_cadena+elemento
    return nueva_cadena

resultado = generar_n_caracteres(5,'a')
print(resultado)