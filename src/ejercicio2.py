################
# Nombre - @absss03
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas.
"""
# Reemplazar por las funciones del ejercicio


def signo(numero):
    """
    Esta función indica si un numero es positivo, negativo o cero.
    """
    if numero == 0:
        resultado = print('{numero} es cero')
    elif numero+numero == abs(numero)*2:
        resultado = print('{numero} es positivo')
    elif numero+numero != abs(numero)*2:
        resultado = print('{numero} es negativo')
    
    return resultado

if __name__ == "__main__":
    
    signo(numero=0)

