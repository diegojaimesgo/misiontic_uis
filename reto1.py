"""
Reto tema 1
¡Qué bueno! Acabas de recibir tu primer salario luego de una ardua jornada de trabajo. Piensas por unos instantes en lo que vas hacer con el dinero que has recibido. 
De manera casi inmediata, vienen a tu mente varias ideas; sin embargo, como responsable que eres decides la forma en la que distribuirás el dinero:

Un 30% para el pago del alquiler del lugar donde estás viviendo,
Un 15% para el pago de los servicios,
10% lo dedicarás para salir con la pareja,
y 5% lo vas a ahorrar en la alcancía.
El dinero restante debe ser destinado para el mercado... pero ¿Cómo puedo hacer para hallar ese valor cada vez que me paguen?

Planteamiento del reto
Con respecto a la situación planteada, ¿De qué manera crees que se puede llegar a automatizar el proceso descrito desde un lenguaje de programación, 
de tal forma que no tengas que volver a realizar los cálculos de presupuesto cada vez que te llegue un salario?
"""

salario = int (input ("Ingresa el salario: "))

presupuesto = salario * 0.60
mercado = salario - presupuesto

print ("El dinero dedicado para mercar es: ", str(mercado))