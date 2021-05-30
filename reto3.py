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
