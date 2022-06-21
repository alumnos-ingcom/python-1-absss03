################
# Nombre - @absss03
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que haga la suma entre dos números enteros sin hacer la 
operación de manera directa. Esto quiere decir que para hacer la suma entre 4 y 3, 
las operaciones resultantes deberán ser 4+1+1+1.
La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""
# Reemplazar por las funciones del ejercicio


def suma_lenta(numero, otro_numero):
    """
    Esta función realiza incrementa un numero en 1 n veces.
    """
    contador = 0
    suma=numero
    if otro_numero > 0:
        while contador < otro_numero:
            suma+= 1
            contador += 1 
    else:
        while contador > otro_numero:
            suma-= 1
            contador -= 1
  
    return suma


if __name__ == "__main__":
    
    suma_lenta(numero=0, otro_numero=0)
