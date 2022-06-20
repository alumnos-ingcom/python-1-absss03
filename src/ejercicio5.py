################
# Nombre - @absss03
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
"""
# Reemplazar por las funciones del ejercicio


def division_lenta(dividendo, divisor):
    """
    Esta función realiza una division mediante restas sucesivas.
    """

    sigue_restando= True
    resultado=0
    while sigue_restando:
        dividendo=dividendo-divisor
        resultado+=1
    if dividendo < divisor:
            sigue_restando= False

    return resultado, dividendo



if __name__ == "__main__":
   
    division_lenta(dividendo=10, divisor=3)

