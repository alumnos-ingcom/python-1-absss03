################
# Nombre - @absss03
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""
# Reemplazar por las funciones del ejercicio


def compara(numero, otro_numero):
    """
    Esta función compara dos numeros e indica cual es el mayor.
    """  

    if numero - otro_numero == 0:
        status= 0
    elif numero - otro_numero > 0:
         status = 1
    else:
        status = -1

    return status

if __name__ == "__main__":
    
    resultado=compara(numero=0, otro_numero=0)