################
# Nombre - @absss03
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Enunciado del ejercicio
"""
# Reemplazar por las funciones del ejercicio

def convertir_a_fahrenheit(centigrados):
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    
    fahrenheit = float((centigrados*(9/5))+32)
    return fahrenheit

def convertir_a_centigrados(fahrenheit):
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    centigrados = float((fahrenheit-32)*(5/9))
    return centigrados


if __name__ == "__main__":

    convertir_a_fahrenheit(centigrados=0)
    
    convertir_a_centigrados(fahrenheit=32)
    