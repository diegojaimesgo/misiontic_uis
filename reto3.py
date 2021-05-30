"""
Reto tema 3
El aplicativo debe cumplir los siguientes requerimientos: 
HISTORIA 1. Solicitar usuario y contraseña: Como usuario, requiero acceder a la aplicación a través del ingreso de usuario y contraseña con el fin de usar el programa.
Se debe validar que las credenciales sean correctas y se debe permitir cuatro intentos máximos. Cada intento fallido debe indicarse con un mensaje "Credenciales incorrectas". 
Luego de los cuatro intentos fallidos se debe presentar un mensaje "Has agotado la cantidad de intentos, por favor inicie de nuevo el programa" y se debe terminar el aplicativo. El usuario predefinido es "admin" y la contraseña es "MisionTic2021"
HISTORIA 2. Presentar menú principal: Como usuario autenticado, requiero poder seleccionar una opción de una lista tipo menú para acceder a una de las funciones que ofrece el 
programa. Al acceder a la aplicación con las credenciales correctas, se debe mostrar un menú con la siguiente estructura: 
"
------Menú de registro de personal-----
1. Registrar ingreso de empleado.
2. Ver empleados ingresados.
3. Registrar ingreso de visitantes.
4. Ver visitantes ingresados.
0. Salir
"
Se debe dejar líneas en blanco arriba y abajo del menú para mejorar la presentación. Bajo el menú, debe presentarse un mensaje de orientación al usuario: 
"Ingresa un número válido de opción del menú: ". El menú debe mostrarse hasta que el usuario digite una opción válida o determine salir. Luego de seleccionar una opción válida
y acceder a alguna función, debe volver a presentar el menú. 
Si se selecciona una opción incorrecta se debe presentar un mensaje al usuario: "Por favor ingresa una opción válida" y volver a presentar el menú. Al escoger la opción 0,
se presentará un mensaje de despedida "¡Hasta luego!" y se terminará el programa.
HISTORIA 3. Añadir empleados al registro: Como usuario autenticado, necesito registrar la información de los nombres de los empleados que ingresan a la sede de la compañía
para llevar control de sus accesos.
Al seleccionar la opción 1 se deben guardar el registro del empleado que ingresa, de manera iterativa, es decir, el usuario podrá registrar tantos empleados como se requieran,
sin necesidad de ingresar cada vez al menú principal. Se dejará de ingresar empleados cuando el usuario ingrese el texto "SALIR". Se debe presentar un mensaje de orientación
al usuario para ingresar la información de cada empleado "Ingresa el nombre del empleado (Si no deseas agregar más, digita SALIR): ".
HISTORIA 4. Visualizar registro de empleados: Como usuario autenticado, necesito visualizar la lista de los empleados que se han registrado en la aplicación para llevar 
control de sus accesos.
Al seleccionar la opción 2, se debe visualizar los datos de los empleados que se registraron. Los datos de los empleados se deben mostrar separados únicamente por comas.
HISTORIA 5. Añadir visitantes al registro: Como usuario autenticado, necesito registrar la información de los nombres de los visitantes que ingresan a la sede de la compañía
para llevar control de sus accesos.
Al seleccionar la opción 3, se deben guardar el registro de visitante quién ingresa, de manera iterativa, es decir, el usuario podrá registrar tantos visitantes como se
requieran, sin necesidad de ingresar cada vez al menú principal. Se dejará de ingresar visitantes cuando el usuario ingrese el texto "SALIR". Se debe presentar un mensaje
de orientación al usuario para ingresar la información de cada visitante "Ingresa el nombre del visitante (Si no deseas agregar más, digita SALIR): "
HISTORIA 6. Visualizar registro de visitantes: Como usuario autenticado, necesito visualizar la lista de los visitantes que se han registrado en la aplicación para llevar
control de sus accesos.
Al seleccionar la opción 4, se debe visualizar los datos de los visitantes. Los datos de los visitantes se deben mostrar separados únicamente por comas.
"""

#Variables con los códigos de acceso:
user = ("admin")
clave = ("MisionTic2021")

#Inicializar contador de intentos e iniciar la bandera en false:
cont = 0
bandera_acceso = False

#Variable string menú
bandeja_menu = ("\n------Menú de registro de personal-----\n1. Registrar ingreso de empleado.\n2. Ver empleados ingresados.\n3. Registrar ingreso de visitantes.\n4. Ver visitantes ingresados.\n\n0. Salir\n")

#Opciones 1 y 2: Variables para registrar empleados:
nuevo_empleado = ""
registro_empleados = ""

#Opciones 3 y 4: Variables para registrar visitantes:
nuevo_visitante = ""
registro_visitantes = ""

#Preguntar códigos de acceso:
while (cont < 4 and bandera_acceso == False) :
    intento_user = input("Usuario: ")
    intento_clave = input("Contraseña: ")


#Validar datos de acceso (si entra con usuario y contraseña):
    while (intento_user == user and intento_clave == clave):
        print (bandeja_menu)
        bandera_acceso = True
        #Inicializar el menú       
        menu = int (input ("Ingresa un número válido de opción del menú: "))
        
        #Opción 1 = Registro de empleados:
        while (menu ==1):
            nuevo_empleado = input("Ingresa el nombre del empleado (Si no deseas agregar más, digita la palabra SALIR):")
            if nuevo_empleado != "SALIR":
                    registro_empleados = registro_empleados + nuevo_empleado + ", "
            else:
                break
        #Opción 2 = Visualizar registro de empleados:
        while (menu ==2):
            print (registro_empleados)
            break
        
        #Opción 3 = Registro de visitantes:
        while (menu ==3):
            nuevo_visitante = input("Ingresa el nombre del visitante (Si no deseas agregar más, digita la palabra SALIR): ")
            if nuevo_visitante != "SALIR":
                    registro_visitantes = registro_visitantes + nuevo_visitante + ", "
            else:
                break

        #Opción 4 = Visualizar registro de visitantes:
        while (menu ==4):
            print (registro_visitantes)
            break

        #Opción 0 = Salida del programa
        while (menu ==0):
            print ("¡Hasta luego!")
            exit ()

       #Si no entra al menú  
        while menu != 4 and menu != 3 and menu != 2 and menu != 1 and menu != 0:
            print("Por favor ingresa una opción válida")
            break

    #Validar datos de acceso (no entra con usuario y contraseña, salida del programa debido a los errores)
    else:
        print ("Credenciales incorrectas")
        cont = cont + 1
        if cont == 4:
            print ("Has agotado la cantidad de intentos, por favor inicie de nuevo el programa")
