"""
3. Escribir una función que tome un carácter y devuelva
True si es una vocal, de lo contrario devuelve False.
"""

def es_vocal (letra: str):

    """Dado una letra retorna si es vocal

        Args:
            letra (str): letra a analizar
        Returns:
            boolean: True en caso de ser vocal
            de lo contrario False
        """
    if(len(letra)>1):
        raise Exception("Debe ingresar una sola letra")
    return letra.lower() in ['a','e','i','o','u']


resultado = es_vocal('r')
print(resultado)
resultado = es_vocal('e')
print(resultado)
resultado = es_vocal('es')
print(resultado)