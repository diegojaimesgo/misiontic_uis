"""
Reto tema 4
En una granja acaban de adquirir una máquina que le permitirá a una empresa de huevos aumentar la rapidez con la que son dispuestos sus productos para la distribución al usuario final. Se requiere un ingeniero de sistemas  para que programe esta máquina bajo ciertos estándares.

Los huevos son clasificados según su calidad y su peso. Para identificar la calidad de los huevos existen 6 referencias que se documentan así: Jumbo, AAA, AA, A, B y C. 

Los huevos son clasificados según su peso, teniendo en cuenta las siguientes reglas:

Huevos tipo C cuyo peso es menor a 46.0 g
Huevos tipo B cuyo peso va desde los 46.0 g hasta un peso menor de 53.0 g.
Huevos tipo A cuyo peso va desde los 53.0 g hasta un peso menor de 60.0 g.
Huevos tipo AA cuyo peso va desde los 60.0 g. hasta un peso menor de 67.0 g.
Huevos tipo AAA cuyo peso va desde los 67.0 g. hasta un peso menor de 78.0 g.
Huevos Jumbo cuyo peso es mayor o igual a 78.0 g.
Escriba una función llamada clasificar_huevos(), cuyo argumento de entrada recibe una lista de datos tipo flotantes asociada al peso de un conjunto de huevos. La lista puede tener cualquier número indeterminado de datos. Un ejemplo de esta lista de datos puede ser:

[46.5, 60.8, 58.7, 70.0, 49.8, 83.1, 52.3, 53.6, 81.7, 55.9, 67.9, 70, 43.2, 65.4, 61.9, 63.9, 44.7, 76.6]

donde cada ítem como se mencionó, está asociado al peso de cada huevo, es decir el primer ítem pertenece a un huevo que pesa 46.5 gr. La función debe ser capaz de clasificar los huevos de acuerdo al peso que se especifique en la lista anteriormente mencionada. Los huevos deben ser clasificados si son C, B, A, AA, AAA o si son Jumbo. Es decir el primer huevo pesa 46.5 gr lo que indica que el huevo es de categoría B.

Al clasificar los huevos determine el total de huevos de cada uno de los tipos de huevos, C, B, A, AA, AAA y Jumbo. Habiendo determinado el número de huevos de acuerdo a cada clasificación, desarrolle una solución adicional para calcular cuántos empaques completos de huevos se pueden obtener para cada una de las categorías, considerando que los huevos tipo B y C se empacan en bandejas de 60 huevos, los huevos de tipo A en bandejas de 30 huevos, los tipo AA en grupos de 24 huevos, y los tipo AAA y Jumbo en grupos de 12 huevos. 

La función clasificar_huevos() debe retornar una lista de directorios con la siguiente estructura:

[

{'tipo_huevo': 'Jumbo', 'numero_huevos': 106, 'numero_bandejas': 8},

{'tipo_huevo': 'AAA', 'numero_huevos': 158, 'numero_bandejas': 13},

{'tipo_huevo': 'AA', 'numero_huevos': 104, 'numero_bandejas': 4},

{'tipo_huevo': 'A', 'numero_huevos': 92, 'numero_bandejas': 3},

{'tipo_huevo': 'B', 'numero_huevos': 170, 'numero_bandejas': 2},

{'tipo_huevo': 'C', 'numero_huevos': 127, 'numero_bandejas': 2}

]

Debe tenerse en cuenta el orden de cada una de las distintas clases de huevos. 

"""


def clasificar_huevos(lista_x_huevos):

    tipo_C = 0
    tipo_B = 0
    tipo_A = 0
    tipo_AA = 0
    tipo_AAA = 0
    tipo_Jumbo = 0

    numero_bandejas_C = 0
    numero_bandejas_B = 0
    numero_bandejas_A = 0
    numero_bandejas_AA = 0
    numero_bandejas_AAA = 0
    numero_bandejas_Jumbo = 0


    lista_diccionarios = []
    diccionario_Jumbo = {"tipo_huevo": "Jumbo", "numero_huevos": 0, "numero_bandejas": 0}
    diccionario_AAA = {"tipo_huevo": "AAA", "numero_huevos": 0, "numero_bandejas": 0}
    diccionario_AA = {"tipo_huevo": "AA", "numero_huevos": 0, "numero_bandejas": 0}
    diccionario_A = {"tipo_huevo": "A", "numero_huevos": 0, "numero_bandejas": 0}
    diccionario_B = {"tipo_huevo": "B", "numero_huevos": 0, "numero_bandejas": 0}
    diccionario_C = {"tipo_huevo": "C", "numero_huevos": 0, "numero_bandejas": 0}
        

    for x in range (0, len(lista_x_huevos)):
        if lista_x_huevos[x] < 46.0:
            tipo_C = tipo_C + 1
            numero_bandejas_C = int(tipo_C/60)
            diccionario_C = {"tipo_huevo": "C", "numero_huevos": tipo_C, "numero_bandejas": numero_bandejas_C}

        elif lista_x_huevos[x] >= 46.0 and lista_x_huevos[x] < 53.0:
            tipo_B = tipo_B + 1
            numero_bandejas_B = int(tipo_B/60)
            diccionario_B = {"tipo_huevo": "B", "numero_huevos": tipo_B, "numero_bandejas": numero_bandejas_B}

        elif lista_x_huevos[x] >= 53.0 and lista_x_huevos[x] < 60.0:
            tipo_A = tipo_A + 1
            numero_bandejas_A = int(tipo_A/30)
            diccionario_A = {"tipo_huevo": "A", "numero_huevos": tipo_A, "numero_bandejas": numero_bandejas_A}

        elif lista_x_huevos[x] >= 60.0 and lista_x_huevos[x] < 67.0:
            tipo_AA = tipo_AA + 1
            numero_bandejas_AA = int(tipo_AA/24)
            diccionario_AA = {"tipo_huevo": "AA", "numero_huevos": tipo_AA, "numero_bandejas": numero_bandejas_AA}

        elif lista_x_huevos[x] >= 67.0 and lista_x_huevos[x] < 78.0:
            tipo_AAA = tipo_AAA + 1
            numero_bandejas_AAA = int(tipo_AAA/12)
            diccionario_AAA = {"tipo_huevo": "AAA", "numero_huevos": tipo_AAA, "numero_bandejas": numero_bandejas_AAA}

        else:
            tipo_Jumbo = tipo_Jumbo + 1
            numero_bandejas_Jumbo = int(tipo_Jumbo/12)
            diccionario_Jumbo = {"tipo_huevo": "Jumbo", "numero_huevos": tipo_Jumbo, "numero_bandejas": numero_bandejas_Jumbo}

    lista_diccionarios.append(diccionario_Jumbo)
    lista_diccionarios.append(diccionario_AAA)
    lista_diccionarios.append(diccionario_AA)
    lista_diccionarios.append(diccionario_A)
    lista_diccionarios.append(diccionario_B)
    lista_diccionarios.append(diccionario_C)

    return lista_diccionarios


print(clasificar_huevos([46.5, 60.8, 58.7, 70, 49.8, 40.9, 51.9, 65.7, 73.4, 41.8, 67.9, 49.2, 78.7, 40.8, 64.6, 63.5, 48.7, 63.2, 84, 46.7, 57.9, 44.2, 83.5, 45.5, 72.2, 52.4, 52.2, 76.2, 72.9, 60.2, 49.2, 59.1, 52.1, 54.9, 59.1, 73.4, 54.5, 78.2, 65, 55.9, 46.8, 69.3, 65, 44, 72.2, 66.1, 45.3, 75, 68.8, 52.3, 82.6, 67.2, 82.6, 49.1, 81.6, 48, 46.4, 81.7, 65.1, 51.8, 69.3, 48.3, 65.2, 45, 40.4, 84.5, 51.1, 83.1, 60.6, 72.4, 40.4, 49.3, 45.5, 46.8, 65, 70.8, 44, 68.3, 78.1, 58.2, 78, 40.9, 63.8, 46.3, 40.3, 80, 52.7, 82.3, 73.8, 43.6, 66.8, 41.6, 63.1, 44, 64.4, 63, 49.2, 59.4, 80, 47.6, 52, 52, 58, 50.3, 75.8, 59.9, 40.3, 77.4, 66.4, 65.4, 51.3, 44.4, 83.1, 52.3, 53.6, 81.7, 55.9, 67.9, 70, 43.2, 65.4, 61.9, 63.9, 44.7, 76.6, 57.2, 44.3, 56.4, 40.4, 52, 76.6, 78.6, 84.7, 50.6, 85, 51.4, 40, 77, 68.7, 48.3, 75.8, 70.8, 71.3, 50.2, 63.4, 44.5, 44.8, 57.1, 41.5, 84.3, 50.1, 50.1, 49.8, 46.5, 60.8, 58.7, 70, 49.8, 73.3, 81, 79.8, 73.3, 82.6, 50.4, 61.1, 56.1, 47.4, 84.1, 67.8, 48.2, 81.6, 48.5, 79.8, 48.8, 66, 70.5, 51.9, 63.5, 54.3, 52.7, 45.7, 83, 71.7, 52.9, 54, 41.3, 48.7, 53.1, 72.3, 64.7, 49.3, 84.3, 40.2, 74, 63.5, 80.6, 62.1, 64.5, 62.6, 83.1, 73.9, 66.3, 69.9, 42, 59, 52.9, 45.4, 72.7, 54.4, 42.3, 46.6, 79.7, 77.6, 50, 58.3, 46.7, 41, 65.6, 77.4, 44, 71.8, 58.8, 56.3, 41.8, 78.5, 57.6, 51.7, 46.7, 65.8, 82, 51.9, 40.1, 54.5, 73.4, 43.6, 44.5, 74.7, 84.6, 71.6, 65.3, 77.9, 70.6, 62.8, 50.5, 84.1, 57.3, 45.4, 66.1, 84.6, 46.1, 77.8, 69.2, 72.4, 45.1, 73.2, 80.5, 46.8, 62.6, 47.9, 51.5, 69.1, 54.2, 81.5, 42.4, 68.5, 56.8, 41.8, 44.2, 46.7, 42.2, 48.1, 59.4, 77.9, 41.8, 48.9, 71.1, 82.9, 70.8, 79, 41.6, 64.5, 79.3, 69.2, 51.6, 49.8, 68.8, 43.4, 78.6, 67.5, 44.8, 57.1, 49.4, 53.5, 42.8, 81.3, 59.9, 62.3, 61.5, 58.1, 48.6, 59.5, 51.5, 47.4, 84.4, 73.1, 50.7, 60.9, 67.7, 73.3, 41.2, 61.4, 57, 42.4, 79.6, 78.7, 79, 43.1, 74.9, 52.4, 81.9, 58.7, 73.9, 73.1, 48.5, 68.3, 44.9, 73, 63.5, 70.3, 42.1, 56.2, 76.3, 49.2, 47.5, 84.4, 52.1, 57.9, 78.3, 73.2, 40.6, 58.8, 74.4, 46.7, 82.3, 62.7, 49, 53.7, 84.9, 57, 46.7, 84, 59.5, 45.6, 79, 61.2, 47.8, 51.4, 40.9, 42.8, 46.5, 60.8, 58.7, 70, 49.8, 73.3, 81, 79.8, 73.3, 82.6, 50.4, 61.1, 56.1, 47.4, 84.1, 67.8, 48.2, 81.6, 48.5, 79.8, 48.8, 66, 70.5, 51.9, 63.5, 54.3, 52.7, 45.7, 83, 71.7, 52.9, 54, 41.3, 48.7, 53.1, 72.3, 64.7, 49.3, 84.3, 40.2, 74, 63.5, 80.6, 62.1, 64.5, 62.6, 83.1, 73.9, 66.3, 69.9, 42, 59, 52.9, 45.4, 72.7, 54.4, 42.3, 46.6, 79.7, 77.6, 50, 58.3, 46.7, 41, 65.6, 77.4, 44, 71.8, 58.8, 56.3, 41.8, 78.5, 57.6, 51.7, 46.7, 65.8, 82, 51.9, 40.1, 54.5, 73.4, 43.6, 44.5, 74.7, 84.6, 71.6, 65.3, 77.9, 70.6, 62.8, 50.5, 84.1, 57.3, 45.4, 66.1, 84.6, 46.1, 77.8, 69.2, 72.4, 45.1, 73.2, 80.5, 46.8, 62.6, 47.9, 51.5, 69.1, 54.2, 81.5, 42.4, 68.5, 56.8, 41.8, 44.2, 46.7, 42.2, 48.1, 59.4, 77.9, 41.8, 48.9, 71.1, 82.9, 70.8, 79, 41.6, 64.5, 79.3, 69.2, 51.6, 49.8, 68.8, 43.4, 78.6, 67.5, 44.8, 57.1, 49.4, 53.5, 42.8, 81.3, 59.9, 46.3, 63.3, 80.1, 44.9, 80.9, 71.3, 46.9, 50.7, 72.8, 63.3, 46.7, 46.7, 46.8, 76.6, 50, 65.6, 75, 78, 71.3, 65.2, 80.2, 62.7, 50.9, 66.8, 52.9, 62.8, 77.1, 40.8, 64, 70.3, 46.2, 49.1, 73.9, 44.5, 78.7, 77.8, 50.3, 40.5, 60.1, 60.9, 48.8, 55.6, 49, 46, 65, 57.9, 69.4, 44.7, 42.1, 82.5, 44.4, 46.7, 73.7, 55.2, 50, 63.8, 64.5, 76.6, 79, 82.7, 42.7, 46.3, 77.3, 60.7, 77.7, 66.2, 79.4, 43.4, 54.7, 53.2, 52.2, 68.8, 52.2, 50.9, 74.3, 53.8, 76.1, 49.3, 54.2, 57.3, 44.4, 55, 66.1, 40.5, 73.3, 54.9, 41.6, 40.2, 66.7, 69.1, 42.9, 42.8, 65.1, 57.3, 40.9, 72.8, 65.9, 46.5, 60.8, 58.7, 70, 49.8, 48.5, 73, 73.6, 77.6, 78.2, 43.4, 64.1, 54.8, 44, 63.3, 65.1, 52.9, 62.3, 77, 70.1, 42, 66.7, 73.9, 46.2, 57.8, 75.8, 49.8, 80, 46, 44.8, 47.1, 80.9, 84.4, 47.7, 50.9, 73.9, 46.2, 44.1, 80.4, 61, 57.1, 40.6, 80.4, 42, 75.9, 75.5, 56.2, 52.5, 80.2, 47.5, 44.2, 77.1, 41.2, 51.2, 83.3, 50.5, 42.5, 85, 72.6, 48.8, 43.3, 74.8, 77.7, 44.3, 83.5, 84.9, 43.7, 65.2, 40.9, 80.6, 51, 68.9, 72.7, 52.6, 61.6, 64.6, 81.9, 45.6, 49, 66.8, 41.7, 73.8, 69.5, 67, 58.8, 45.1, 51.7, 43.9, 73.7, 70.1, 45.6, 79, 56, 49.7, 43.4, 54.1, 48.3, 76.5, 65, 44.3, 46.4, 52.2, 58.1, 49.8, 69.1, 52.1, 43.7, 60.2, 68, 77.4, 49.4, 84.9, 59.2, 44.5, 61.2, 71.5, 71.1, 40.3, 49.6, 60.1, 72.9, 53.3, 56, 72.6, 65.2, 84, 68.7, 54.9, 58.6, 55, 41.4, 49.9, 66.1, 50.1, 75.3, 77.5, 43.1, 45.3, 47.5, 60.6, 47.4, 83.8, 82.4, 46.5, 67, 65.1, 45.2, 67.3, 54.3, 69.3, 45.8, 50.7, 62.6, 47.1, 80.7, 54.7, 48.7, 48]))
[46.5, 60.8, 58.7, 70, 49.8, 40.9, 51.9, 65.7, 73.4, 41.8, 67.9, 49.2, 78.7, 40.8, 64.6, 63.5, 48.7, 63.2, 84, 46.7, 57.9, 44.2, 83.5, 45.5, 72.2, 52.4, 52.2, 76.2, 72.9, 60.2, 49.2, 59.1, 52.1, 54.9, 59.1, 73.4, 54.5, 78.2, 65, 55.9, 46.8, 69.3, 65, 44, 72.2, 66.1, 45.3, 75, 68.8, 52.3, 82.6, 67.2, 82.6, 49.1, 81.6, 48, 46.4, 81.7, 65.1, 51.8, 69.3, 48.3, 65.2, 45, 40.4, 84.5, 51.1, 83.1, 60.6, 72.4, 40.4, 49.3, 45.5, 46.8, 65, 70.8, 44, 68.3, 78.1, 58.2, 78, 40.9, 63.8, 46.3, 40.3, 80, 52.7, 82.3, 73.8, 43.6, 66.8, 41.6, 63.1, 44, 64.4, 63, 49.2, 59.4, 80, 47.6, 52, 52, 58, 50.3, 75.8, 59.9, 40.3, 77.4, 66.4, 65.4, 51.3, 44.4, 83.1, 52.3, 53.6, 81.7, 55.9, 67.9, 70, 43.2, 65.4, 61.9, 63.9, 44.7, 76.6, 57.2, 44.3, 56.4, 40.4, 52, 76.6, 78.6, 84.7, 50.6, 85, 51.4, 40, 77, 68.7, 48.3, 75.8, 70.8, 71.3, 50.2, 63.4, 44.5, 44.8, 57.1, 41.5, 84.3, 50.1, 50.1, 49.8, 46.5, 60.8, 58.7, 70, 49.8, 73.3, 81, 79.8, 73.3, 82.6, 50.4, 61.1, 56.1, 47.4, 84.1, 67.8, 48.2, 81.6, 48.5, 79.8, 48.8, 66, 70.5, 51.9, 63.5, 54.3, 52.7, 45.7, 83, 71.7, 52.9, 54, 41.3, 48.7, 53.1, 72.3, 64.7, 49.3, 84.3, 40.2, 74, 63.5, 80.6, 62.1, 64.5, 62.6, 83.1, 73.9, 66.3, 69.9, 42, 59, 52.9, 45.4, 72.7, 54.4, 42.3, 46.6, 79.7, 77.6, 50, 58.3, 46.7, 41, 65.6, 77.4, 44, 71.8, 58.8, 56.3, 41.8, 78.5, 57.6, 51.7, 46.7, 65.8, 82, 51.9, 40.1, 54.5, 73.4, 43.6, 44.5, 74.7, 84.6, 71.6, 65.3, 77.9, 70.6, 62.8, 50.5, 84.1, 57.3, 45.4, 66.1, 84.6, 46.1, 77.8, 69.2, 72.4, 45.1, 73.2, 80.5, 46.8, 62.6, 47.9, 51.5, 69.1, 54.2, 81.5, 42.4, 68.5, 56.8, 41.8, 44.2, 46.7, 42.2, 48.1, 59.4, 77.9, 41.8, 48.9, 71.1, 82.9, 70.8, 79, 41.6, 64.5, 79.3, 69.2, 51.6, 49.8, 68.8, 43.4, 78.6, 67.5, 44.8, 57.1, 49.4, 53.5, 42.8, 81.3, 59.9, 62.3, 61.5, 58.1, 48.6, 59.5, 51.5, 47.4, 84.4, 73.1, 50.7, 60.9, 67.7, 73.3, 41.2, 61.4, 57, 42.4, 79.6, 78.7, 79, 43.1, 74.9, 52.4, 81.9, 58.7, 73.9, 73.1, 48.5, 68.3, 44.9, 73, 63.5, 70.3, 42.1, 56.2, 76.3, 49.2, 47.5, 84.4, 52.1, 57.9, 78.3, 73.2, 40.6, 58.8, 74.4, 46.7, 82.3, 62.7, 49, 53.7, 84.9, 57, 46.7, 84, 59.5, 45.6, 79, 61.2, 47.8, 51.4, 40.9, 42.8, 46.5, 60.8, 58.7, 70, 49.8, 73.3, 81, 79.8, 73.3, 82.6, 50.4, 61.1, 56.1, 47.4, 84.1, 67.8, 48.2, 81.6, 48.5, 79.8, 48.8, 66, 70.5, 51.9, 63.5, 54.3, 52.7, 45.7, 83, 71.7, 52.9, 54, 41.3, 48.7, 53.1, 72.3, 64.7, 49.3, 84.3, 40.2, 74, 63.5, 80.6, 62.1, 64.5, 62.6, 83.1, 73.9, 66.3, 69.9, 42, 59, 52.9, 45.4, 72.7, 54.4, 42.3, 46.6, 79.7, 77.6, 50, 58.3, 46.7, 41, 65.6, 77.4, 44, 71.8, 58.8, 56.3, 41.8, 78.5, 57.6, 51.7, 46.7, 65.8, 82, 51.9, 40.1, 54.5, 73.4, 43.6, 44.5, 74.7, 84.6, 71.6, 65.3, 77.9, 70.6, 62.8, 50.5, 84.1, 57.3, 45.4, 66.1, 84.6, 46.1, 77.8, 69.2, 72.4, 45.1, 73.2, 80.5, 46.8, 62.6, 47.9, 51.5, 69.1, 54.2, 81.5, 42.4, 68.5, 56.8, 41.8, 44.2, 46.7, 42.2, 48.1, 59.4, 77.9, 41.8, 48.9, 71.1, 82.9, 70.8, 79, 41.6, 64.5, 79.3, 69.2, 51.6, 49.8, 68.8, 43.4, 78.6, 67.5, 44.8, 57.1, 49.4, 53.5, 42.8, 81.3, 59.9, 46.3, 63.3, 80.1, 44.9, 80.9, 71.3, 46.9, 50.7, 72.8, 63.3, 46.7, 46.7, 46.8, 76.6, 50, 65.6, 75, 78, 71.3, 65.2, 80.2, 62.7, 50.9, 66.8, 52.9, 62.8, 77.1, 40.8, 64, 70.3, 46.2, 49.1, 73.9, 44.5, 78.7, 77.8, 50.3, 40.5, 60.1, 60.9, 48.8, 55.6, 49, 46, 65, 57.9, 69.4, 44.7, 42.1, 82.5, 44.4, 46.7, 73.7, 55.2, 50, 63.8, 64.5, 76.6, 79, 82.7, 42.7, 46.3, 77.3, 60.7, 77.7, 66.2, 79.4, 43.4, 54.7, 53.2, 52.2, 68.8, 52.2, 50.9, 74.3, 53.8, 76.1, 49.3, 54.2, 57.3, 44.4, 55, 66.1, 40.5, 73.3, 54.9, 41.6, 40.2, 66.7, 69.1, 42.9, 42.8, 65.1, 57.3, 40.9, 72.8, 65.9, 46.5, 60.8, 58.7, 70, 49.8, 48.5, 73, 73.6, 77.6, 78.2, 43.4, 64.1, 54.8, 44, 63.3, 65.1, 52.9, 62.3, 77, 70.1, 42, 66.7, 73.9, 46.2, 57.8, 75.8, 49.8, 80, 46, 44.8, 47.1, 80.9, 84.4, 47.7, 50.9, 73.9, 46.2, 44.1, 80.4, 61, 57.1, 40.6, 80.4, 42, 75.9, 75.5, 56.2, 52.5, 80.2, 47.5, 44.2, 77.1, 41.2, 51.2, 83.3, 50.5, 42.5, 85, 72.6, 48.8, 43.3, 74.8, 77.7, 44.3, 83.5, 84.9, 43.7, 65.2, 40.9, 80.6, 51, 68.9, 72.7, 52.6, 61.6, 64.6, 81.9, 45.6, 49, 66.8, 41.7, 73.8, 69.5, 67, 58.8, 45.1, 51.7, 43.9, 73.7, 70.1, 45.6, 79, 56, 49.7, 43.4, 54.1, 48.3, 76.5, 65, 44.3, 46.4, 52.2, 58.1, 49.8, 69.1, 52.1, 43.7, 60.2, 68, 77.4, 49.4, 84.9, 59.2, 44.5, 61.2, 71.5, 71.1, 40.3, 49.6, 60.1, 72.9, 53.3, 56, 72.6, 65.2, 84, 68.7, 54.9, 58.6, 55, 41.4, 49.9, 66.1, 50.1, 75.3, 77.5, 43.1, 45.3, 47.5, 60.6, 47.4, 83.8, 82.4, 46.5, 67, 65.1, 45.2, 67.3, 54.3, 69.3, 45.8, 50.7, 62.6, 47.1, 80.7, 54.7, 48.7, 48]