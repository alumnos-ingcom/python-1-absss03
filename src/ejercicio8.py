################
# Nombre - @absss03
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un numero indicado es Primo.
"""

from src.ejercicio5 import division_lenta

def es_primo(numero):
    """
    Esta función es la que se encarga de indicar si un numero es primo o no 
    retornando True o False respectivamente.
    """

    primo=True
    for i in range(2,numero):
        cociente, resto=division_lenta(numero, i)
        if resto == 0:
            primo=False
  
    return primo

resultado=es_primo(numero=0)

if __name__ == "__main__":
    
    es_primo(numero=7)
