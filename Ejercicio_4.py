"""
4. Escribir una función sum() y una función multip() que sumen
 y multipliquen respectivamente todos los números de una lista.
 Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
 debería devolver 24.
"""
from functools import reduce
from typing import List

def add(a,b):
    return a + b

def mult(a,b):
    return a * b

def sum_custom(lista) -> int :
    """Dado una lista retorna la suma de los elementos

    Args:
        lista (list): lista a sumar

    Returns:
        int : resultado de la suma de los elementos
    """
    resultado = reduce(add, lista)
    return resultado


def mult_custom(lista) -> int:
    """Dado una lista retorna el producto de los elementos

    Args:
        lista (list): elementos a multiplicar

    Returns:
        int : resultado de la multiplicacion de los elementos
    """
    resultado = reduce(mult, lista)
    return resultado

resultado_suma = sum_custom([10,12,3])
print("Resultado suma: "+str(resultado_suma))

resultado_multiplicacion = mult_custom([10,12,3])
print("Resultado Multiplicacion: "+str(resultado_multiplicacion))

"""Otra manera de resolver el ejercicio es mediante
el uso de una estructura for 
"""

def sum_for(lista: List[int]) -> int :
    resultado = 0
    for numero in lista:
        resultado += numero
    return resultado

def mult_for(lista: List[int]) -> int :
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

resultado_suma_2 = sum_for ([10,12,3])
print("Resultado suma con for: "+str(resultado_suma_2))
resultado_multiplicacion_2 = mult_for ([10,12,3])
print("Resultado Multiplicacion con for: "+str(resultado_multiplicacion_2))


