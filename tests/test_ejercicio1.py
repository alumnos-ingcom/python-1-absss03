################
# Nombre - @absss03
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Prueba la funcion de conversion de grados Centigrados a Fahrrenheit y
la de grados Fahrenheit a Centigrados.
"""
from src.ejercicio1 import convertir_a_fahrenheit
from src.ejercicio1 import convertir_a_centigrados

def test_convertir_a_fahrenheit(centigrados):
   """
      Prueba la funcion de conversion de grados Centigrados a Fahrenheit
   """
   valores_de_entrada=[0,31.1111,74.4444,100]
   valores_de_salida=[32,87.99998,165.99992,212]

   for i in range(4):
      centigrados=valores_de_entrada[i]
      fahrenheit=convertir_a_fahrenheit(centigrados)
      if fahrenheit == valores_de_salida[i]:
         print(f'{centigrados} Centigrados equivalen a {fahrenheit} en Fahrenheit')
      else:
         print(f'Error en la conversion de {centigrados} Centigrados a Fahrenheit')


def test_convertir_a_centigrados(fahrenheit):
   """
      Prueba la funcion de conversion de grados Fahrenheit a Centigrados 
   """
   valores_de_entrada=[32,87.99998,165.99992,212]
   valores_de_salida=[0,31.1111,74.4444,100]

   for i in range(4):
      fahrenheit=valores_de_entrada[i]
      centigrados=convertir_a_centigrados(fahrenheit)
      if centigrados == valores_de_salida[i]:
         print(f'{fahrenheit} Fahrenheit equivalen a {centigrados} en Centigrados')
      else:
         print(f'Error en la conversion de {fahrenheit} Fahrenheit a Centigrados')
