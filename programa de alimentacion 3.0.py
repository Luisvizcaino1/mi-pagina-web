
usu_admin = "Admin"
contra_admin = 1234

nombre_aprendiz = "Luis vizcaino"
usu_aprendiz = "1003251790"
contra_aprendiz = 1003251790
raciones_aprendiz = 5

# Variables para almacenar los datos de los aprendices
nombre1, apellido1, cedula1, programa1  = "", "", "", "" 
nombre2, apellido2, cedula2, programa2  = "", "", "", ""
nombre3, apellido3, cedula3, programa3  = "", "", "", ""
nombre4, apellido4, cedula4, programa4  = "", "", "", ""
nombre5, apellido5, cedula5, programa5  = "", "", "", ""
nombre6, apellido6, cedula6, programa6, = "", "", "", ""
nombre7, apellido7, cedula7, programa7, = "", "", "", ""
nombre8, apellido8, cedula8, programa8, = "", "", "", ""
nombre9, apellido9, cedula9, programa9, = "", "", "", ""
nombre10, apellido10, cedula10, programa10,  = "", "", "", ""

print("-------------------------------------------")
print(" Bienvenido al programa de alimentacion")
print("-------------------------------------------")
print("1. ingresar como Administrador ")
print("2: ingresar como aprendiz")
print("-------------------------------------------") 

seleccion = int(input("Elija una opción: "))
if seleccion< 1 or seleccion>2:
     print("Opcion no encontrada")
     print("--------------------------------------")
     print("1. ingresar como Administrador ")
     print("2: ingresar como aprendiz")
     print("--------------------------------------")
     seleccion=int(input("Ingrese el numero de su opcion  "))

if seleccion< 1 or seleccion>2:
     print("Opcion no encontrada")
     print("-------------------------------------")
     print("1. ingresar como Administrador ")
     print("2: ingresar como aprendiz")
     print("--------------------------------")
     seleccion=int(input("Ingrese el numero de la obcion que desea  "))


if seleccion == 1:
    usu = input("Ingrese su usuario: ")
    contra = int(input("Ingrese su contraseña: "))

    if usu == usu_admin and contra == contra_admin:
        print("---------------------------------------")


    else:
        print("Usuario o contraseña incorrectos, intente nuevamente.")
        usu = input("Ingrese su usuario: ")
        contra = int(input("Ingrese su contraseña: "))


    if usu == usu_admin and contra == contra_admin:
        print("Inicio de sesión exitoso.")
        registro = input("¿Desea registrar aprendices? (si/no): ")
        if registro == 'si' or registro =="si":
            cantidad = int(input("Ingrese la cantidad de aprendices a registrar (máximo 10): "))
            for i in range(1, cantidad + 1):
                nombre = input(f"Ingrese el nombre del aprendiz {i}: ")
                apellido = input(f"Ingrese el apellido del aprendiz {i}: ")
                cedula = input(f"Ingrese la cédula del aprendiz {i}: ")
                programa = input(f"Ingrese el programa de formación del aprendiz {i}: ")
                print()
        
                if i == 1:
                    nombre1 = nombre
                    apellido1 = apellido
                    cedula1 = cedula
                    programa1 = programa

                elif i == 2:
                    nombre2 = nombre
                    apellido2 = apellido
                    cedula2 = cedula
                    programa2 = programa

                elif i == 3:
                    nombre3 = nombre
                    apellido3 = apellido
                    cedula3 = cedula
                    programa3 = programa

                elif i == 4:
                    nombre4 = nombre
                    apellido4 = apellido
                    cedula4 = cedula
                    programa4 = programa

                elif i == 5:
                    nombre5 = nombre
                    apellido5 = apellido
                    cedula5 = cedula
                    programa5 = programa

                elif i == 6:
                    nombre6 = nombre
                    apellido6 = apellido
                    cedula6 = cedula
                    programa6 = programa

                elif i == 7:
                    nombre7 = nombre
                    apellido7 = apellido
                    cedula7 = cedula
                    programa7 = programa

                elif i == 8:
                    nombre8 = nombre
                    apellido8 = apellido
                    cedula8 = cedula
                    programa8 = programa

                elif i == 9:
                    nombre9 = nombre
                    apellido9 = apellido
                    cedula9 = cedula
                    programa9 ==programa

                elif i == 10:
                    nombre10 = nombre
                    apellido10 = apellido
                    cedula10 = cedula
                    programa10 = programa
                    
                print("------------------------------------------")
            
            consulta = input("¿Desea consultar los aprendices registrados? (si/no): ")
            if consulta == 'si' or consulta =="SI":
                print("Aprendices registrados:")
                if nombre1 == nombre1:
                    print(f"1: {nombre1} {apellido1}, Cédula: {cedula1}, Programa: {programa1}")
                if nombre2:
                    print(f"2: {nombre2} {apellido2}, Cédula: {cedula2}, Programa: {programa2}")
                if nombre3:
                    print(f"3: {nombre3} {apellido3}, Cédula: {cedula3}, Programa: {programa3}")
                if nombre4:
                    print(f"4: {nombre4} {apellido4}, Cédula: {cedula4}, Programa: {programa4}")
                if nombre5:
                    print(f"5: {nombre5} {apellido5}, Cédula: {cedula5}, Programa: {programa5}")
                if nombre6:
                    print(f"6: {nombre6} {apellido6}, Cédula: {cedula6}, Programa: {programa6}")
                if nombre7:
                    print(f"7: {nombre7} {apellido7}, Cédula: {cedula7}, Programa: {programa7}")
                if nombre8:
                    print(f"8: {nombre8} {apellido8}, Cédula: {cedula8}, Programa: {programa8}")
                if nombre9:
                    print(f"9: {nombre9} {apellido9}, Cédula: {cedula9}, Programa: {programa9}")
                if nombre10:
                    print(f"10: {nombre10} {apellido10}, Cédula: {cedula10}, Programa: {programa10}")
                    print("registros exitosos")
                print("-----------------------------------------------------")
                     
                if not ([nombre1, nombre2, nombre3, nombre4, nombre5, nombre6, nombre7, nombre8, nombre9, nombre10]):
                   print("No hay aprendices registrados.")  
        else:
            print("---------------------------------------------------------")

            print("       MENU DE LA SEMANA   ")
            print("- Dia 1:      Arroz con pescado y ensalada.")
            print("- Dia 2:      Arroz con carne y ensalada.")
            print("- Dia 3:      Arroz con cerdo, ensalada y patacon.")
            print("- Dia 4:      Arroz, pollo y ensalada.")
            print("- Dia 5:      Arroz pezcado y ensalada .")

            print("--------------------------------------------------\n")

    else:
        print("Usuario o contraseña incorrectos otra vez. Se han agotado los intentos. Por favor, inténtelo más tarde.")

elif seleccion == 2:
    print("Bienvenido aprendiz")
    usu = input("Ingrese su usuario: ")
    contra = int(input("Ingrese su contraseña: "))

    if usu == usu_aprendiz and contra == contra_aprendiz:
        pass

    else:
        print("Usuario o contraseña incorrectos, intente nuevamente.")
        usu = input("Ingrese su usuario: ")
        contra = int(input("Ingrese su contraseña: "))

    if usu == usu_aprendiz and contra == contra_aprendiz:
        print(f"Señor {nombre_aprendiz}, su semana de alimentacion es la (1), este es el orden de entrega.")
        print("Semana 1: alimentacion para el programa de ADSO")
        print("Semana 2: alimentacion para el programa de GESTION EMPRESARIAL")
        print("Semana 3: alimentacion para el programa de MULTIMEDIA")
        print("Semana 4: alimentacion para el programa de COCINA")
        
        print("A continuacionn se le mostrara el menu de la semana.  ")


        print("------------------------------------------")
        print("       MENU DE LA SEMANA   ")
        print("- Dia 1:      Arroz , pescado y ensalada.")
        print("- Dia 2:      Arroz con carne y ensalada.")
        print("- Dia 3:      Arroz con cerdo ensalada y patacon.")
        print("- Dia 4:      Arroz, pollo y ensalada.")
        print("- Dia 5:      Arroz, pezcado y ensalada .")

        print("--------------------------------------------------\n")
        print("Desea recibir su comida para el dia 1:")
        comida = input("ingrese su opcion, (si/no): ")


        if comida == "si" or comida=="SI":
            print("------------------------------------------")
            print("PUEDE RECLAMAR SU APOYO ALIMENTARIO  ")
            print("------------------------------------------")
            raciones_aprendiz -= 1
            print (f"Le quedan {raciones_aprendiz} raciones ")
            print("--------------------------------------------------")


        if comida == "no" or comida=="NO":
            print("------------------------------------------")
            print("OK, Se le entregara a otro aprendiz que lo necesite  ")
            print("------------------------------------------")
            raciones_aprendiz -= 1
            print (f"Le quedan {raciones_aprendiz} raciones ")
            print("--------------------------------------------------")
        print("Desea recibir su comida para el dia 2:")
        comida = input("Ingrese su opcion, (si/no): ")

        if comida == "si" or comida =="SI":
            print("------------------------------------------")
            print("PUEDE RECLAMAR SU APOYO ALIMENTARIOS ")
            print("------------------------------------------")
            raciones_aprendiz -= 1
            print (f"Le quedan {raciones_aprendiz} raciones ")
            print("--------------------------------------------------")


        if comida == "no" or comida=="NO":
            print("------------------------------------------")
            print("OK, Se le entregara a otro aprendiz que lo necesite  ")
            print("------------------------------------------")
            raciones_aprendiz -= 1
            print (f"Le quedan {raciones_aprendiz} raciones ")
            print("--------------------------------------------------")    
        print("Desea recibir su comida para el dia 3:")
        comida = input("ingrese su opcion, (si/no): ")  

  
        if comida == "si" or comida=="SI":
            print("------------------------------------------")
            print("PUEDE RECLAMAR SU APOYO ALIMENTARIOS ")
            print("------------------------------------------")
            raciones_aprendiz -= 1
            print (f"Le quedan {raciones_aprendiz} raciones ")
            print("--------------------------------------------------")
            print("--------------------------------------------------")


        if comida == "no" or comida=="NO":
            print("------------------------------------------")
            print("OK, Se le entregara a otro aprendiz que lo necesite  ")
            print("------------------------------------------")
            raciones_aprendiz -= 1
            print (f"Le quedan {raciones_aprendiz} raciones ")
            print("--------------------------------------------------")
        print("Desea recibir su comida para el dia 4:")
        comida = input("ingrese su opcion, (si/no): ")


        if comida == "si" or comida=="SI":
            print("------------------------------------------")
            print("PUEDE RECLAMAR SU APOYO ALIMENTARIOS ")
            print("------------------------------------------\n")
            raciones_aprendiz -= 1
            print (f"Le quedan {raciones_aprendiz} raciones ")
            print("--------------------------------------------------\n")
            print("--------------------------------------------------\n")


        if comida == "no" or comida=="NO":
            print("------------------------------------------")
            print("OK, Se le entregara a otro aprendiz que lo necesite  ")
            print("------------------------------------------\n")
            raciones_aprendiz -= 1
            print (f"Le quedan {raciones_aprendiz} raciones ")
            print("--------------------------------------------------\n")
        print("Desea recibir su comida para el dia 5:")
        comida = input("ingrese su opcion, (si/no): ")


        if comida == "si" or comida=="SI":
            print("------------------------------------------")
            print("PUEDE RECLAMAR SU APOYO ALIMENTARIOS ")
            print("------------------------------------------")
            raciones_aprendiz -= 1
            print (f"Le quedan {raciones_aprendiz} raciones ")
            if raciones_aprendiz==0:
             print("No tiene mas raciones disponibles para esta semana ")
             print("--------------------------------------------------")

        if comida == "no" or comida=="NO":
            print("------------------------------------------")
            print("OK, Se le entregara a otro aprendiz que lo necesite  ")
            print("------------------------------------------")
            raciones_aprendiz -= 1
            print (f"Le quedan {raciones_aprendiz} raciones ")
            print("--------------------------------------------------")