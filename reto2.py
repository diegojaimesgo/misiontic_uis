"""
Planteamiento de la situación

Muchos son los cambios que promueven la pandemia generada por el COVID-19 y sus variantes; por mencionar algunos: la alimentación, el control del peso, etc.
María Fernanda se encuentra preocupada por la salud de su familia, y encuentra un artículo para llevar un control sobre el peso, conocido como “índice de masa corporal” (IMC)
para adultos de 20 años o más.  El IMC permite establecer una clasificación al relacionar el peso en metros con el peso en kilogramos; la relación esta determinada
por el peso (kg) / estatura (mts) elevada a la 2, que determina un índice y a su vez el nivel de peso (bajo peso, normal, sobrepeso y obeso). 

 

IMC

Nivel de peso

Por debajo de 18.5 - Bajo peso
18.5 – 24.9 - Normal
25.0 – 29.9 - Sobrepeso
30.0 o más - Obeso

 

Planteamiento del reto:
Con respecto a la situación planteada, ¿De qué manera crees que María Fernanda puede automatizar el control del nivel de peso para sus familiares con base al IMC?, 
considerando que la frecuencia y cantidad de integrantes del grupo familiar son numerosos, demandando mucho tiempo para realizar los cálculos de forma manual, y la alta probabilidad de equivocarse; 
entonces, María Fernanda decide diseñar un algoritmo desde un lenguaje de programación, que simplifique el tiempo empleado y minimice la probabilidad de error humano al realizar las operaciones a
 cada uno de sus familiares.
"""

peso = float (input ("Ingrese el peso: "))
estatura = float (input ("Ingrese la estatura: "))

imc = peso/(estatura**2)

if imc < 18.5:
    print ("Bajo peso")

elif imc >= 18.5 and imc <= 24.9:
    print ("Normal")

elif imc >= 25 and imc <= 29.9:
    print ("Sobrepeso")

else:
    print ("Obeso")