import random
import string
import re

# Las credenciales del administrador
usu_admin = "Admin"
contra_admin = "1234"

# Estructura para mantener registro de no recepción de comidas por semana
no_recibieron_comida = [[], [], [], [], []]
recibieron_comida = [[], [], [], []]

# Número máximo de intentos permitidos
intentos_maximos = 3

# Lista de usuarios registrados
usuarios_registrados = []

# Lista de usuarios bloqueados
usuarios_bloqueados = []
# Contador para las raciones si que si
contador_si=0
# Contador para raciones si dice que no
contador_no=0
# Raciones por aprendiz
raciones_aprendiz = 5

# Caracteres especiales para el usuario
caracteres_especiales = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', "<", "!!", ">"]

# Lista de programas
programas = [
    [1, "ADSO"],
    [2, "GESTION ADMINISTRATIVA"],
    [3, "GESTION EMPRESARIAL"],
    [4, "ANIMACION 3D"],
    [5, "MULTIMEDIA"],
    [6, "MODISTERIA"],
    [7, "COCINA"],
    [8, "GANADERIA"]
]

while True:
    print(" _____________________________________")
    print("|                                     |")
    print("|           INICIAR COMO:             |")
    print("|_____________________________________|")
    print("|         1. APRENDIZ                 |")
    print("|                                     |")
    print("|         2. ADMINISTRADOR            |")
    print("|                                     |")
    print("|         3. INVITADO                 |")
    print("|                                     |")
    print("|         4.  SALIR                   |")
    print("|_____________________________________|")
    seleccion = input("Elija una opción: ")

    if seleccion == "1":  # Opción para el Aprendiz
        intentos = 0

        while intentos < intentos_maximos:
            print("     ______________________________")
            print("    |   BIENVENIDO APRENDIZ        |")
            print("    |______________________________|")
            print("")
            print("       ESTAS SON SUS OPCIONES  ")
            print("")
            print("     ______________________________")
            print("1.  |       REGISTRARSE            |")
            print("2.  |       INICIAR SESION         |")
            print("3.  |       RECUPERAR CUENTA       |")
            print("4.  |       SALIR                  |")
            print("    |______________________________|")
            print("")
            opcion_aprendiz = input("Ingrese el número de su opción: ")

            if opcion_aprendiz == "1":
                # Registro de nuevo usuario
                while True:
                    nombre = input("Ingrese su nombre: ")
                    valido = True
                    for char in nombre:
                        if char.isdigit():
                            valido = False
                            break
                    if valido:
                        break
                while True:
                    apellido = input("Ingrese su apellido: ")
                    valido = True
                    for char in apellido:
                        if char.isdigit():
                            valido = False
                            break
                    if valido:
                        break

                while True:
                    cedula = input("Ingrese su cédula: ")
                    if cedula.isdigit() and 8 <= len(cedula) <= 10:
                        break
                    else:
                        print("La cédula debe contener entre 8 y 10 dígitos Y no puede contener letras. Inténtelo de nuevo.")

                print("Seleccione su programa de formación:")
                print("------------------------------")
                for programa in programas:
                    print(f"{programa[0]}. {programa[1]}")
                print("------------------------------")
                programa_numero = int(input("Ingrese el número del programa de formación: "))
                programa_nombre = "Desconocido"
                for programa in programas:
                    if programa[0] == programa_numero:
                        programa_nombre = programa[1]
                        break

                semana = f"Semana ({(programa_numero - 1) // 2 + 1})"

                patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                dominios_permitidos = ['gmail.com', 'hotmail.com', 'yahoo.com']

                while True:
                    correo_electronico = input("Ingresa tu correo electrónico: ").strip()
                    if re.match(patron_correo, correo_electronico):
                        dominio = correo_electronico.split('@')[1]
                        if dominio in dominios_permitidos:
                            print("Correo electrónico válido. Acceso permitido.")
                            break
                        else:
                            print("Lo siento, el dominio de correo electrónico no está permitido.")
                    else:
                        print("Formato de correo electrónico inválido. Por favor, inténtalo de nuevo.")

                # Generar usuario único
                usuario_base = nombre[0].lower() + apellido.lower()
                usuario = usuario_base
                contador = 1
                while any(user[5] == usuario for user in usuarios_registrados):
                    usuario += random.choice(caracteres_especiales)
                    contador += 1

                # Generar contraseña aleatoria
                numero_clave = random.randint(1000, 9999)
                letra = random.choice(string.ascii_uppercase)
                clave = f"{letra}{numero_clave:04d}{nombre}"

                # Mostrar datos generados
                print("----------------------------------")
                print(f"Usuario generado: {usuario}")
                print(f"Clave generada: {clave}")

                # Guardar usuario en la lista de usuarios registrados
                nuevo_usuario = [
                    nombre, apellido, cedula, programa_nombre, correo_electronico, usuario, clave, semana
                ]
                usuarios_registrados.append(nuevo_usuario)

                print("")
                print("   EL REGISTRO FUE EXITOSO ")
                print("")
                print("       INICIAR SESION ")

            elif opcion_aprendiz == "2":
                usuario_i = input("Ingrese su usuario: ")
                contraseña_i = input("Ingrese su contraseña: ")

                # Verificar si el usuario está bloqueado
                if usuario_i in [user[5] for user in usuarios_bloqueados]:
                    print("Su cuenta está bloqueada. Por favor, contacte al administrador.")
                    break

                # Verificar credenciales
                usuario_encontrado = None
                for user in usuarios_registrados:
                    if user[5] == usuario_i:
                        usuario_encontrado = user
                        break

                if usuario_encontrado:
                    # Verificar contraseña
                    if contraseña_i == usuario_encontrado[6]:
                        print("")
                        print("")
                        print(f"Bienvenido {usuario_encontrado[0]}")
                        print(f"Señor {usuario_encontrado[0]}, su semana de alimentación es la {usuario_encontrado[7]}.")
                        print("")
                        print(" _____________________________________")
                        print("| ESTOS SON LOS PROGRAMAS BENEFICIADOS|  ")
                        print("|_____________________________________|")
                        
                        for programa in programas:
                            print(f"| {programa[1].ljust(30)} |")
                        
                        print("")
                        print("       SEMANAS DE ALIMENTACION ASIGNADAS PARA LOS PROGRAMAS :")
                        print("")
                        print(" ______________________________________________________________________________")
                        print("|Semana 1: alimentacion para el programa de ADSO, GESTION ADMINISTRATIVA       |")
                        print("|Semana 2: alimentacion para el programa de GESTION EMPRESARIAL, ANIMACION 3D  |")
                        print("|Semana 3: alimentacion para el programa de MULTIMEDIA, MODISTERIA             |")
                        print("|Semana 4: alimentacion para el programa de COCINA, GANADERIA                  |")
                        print("|______________________________________________________________________________|")
                        print("")
                        print("")
                        print("        ESTE ES EL MENU DE LA SEMANA ")
                        print("")
                        print(" _____________________________________________________________")
                        print("|DIA 1 : Lunes     = Arroz de pollo y ensalda.                |" )
                        print("|DIA 2 : Martes    = Arroz con carne y ensalada.              |" )
                        print("|DIA 3 : Miércoles = Arroz con carne molida y papas fritas.   |" )
                        print("|DIA 4 : Jueves    = Arroz con cerdo y ensalada.              |" )
                        print("|DIA 5 : Viernes   = Arroz con pescado frito.                 |" )
                        print("|_____________________________________________________________|")
                        print("")

                        # Obtener el número de la semana del usuario
                        semana_numero = int(usuario_encontrado[7].split()[1][1])

                        if semana_numero == 1:  # Solo para la semana 1
                            print("Desea recibir su comida para este dia:")
                            comida = input("Ingrese su opción, (si/no): ")

                            if comida.lower() == "si":
                                contador_si+=1
                                print("\n------------------------------------------")
                                print("PUEDE RECLAMAR SU APOYO ALIMENTARIO")
                                print("------------------------------------------\n")
                                raciones_aprendiz -= 1
                                print(f"Le quedan {raciones_aprendiz} raciones")
                                print("--------------------------------------------------\n")
                                recibieron_comida[semana_numero - 1].append(usuario_encontrado[5])
                            elif comida.lower() == "no":
                                contador_no+=1
                                # Asignar comida a otro aprendiz automáticamente
                                for i in range(1, len(no_recibieron_comida[semana_numero - 1]) + 1):
                                    if i >= len(no_recibieron_comida[semana_numero - 1]):
                                        no_recibieron_comida[semana_numero - 1].append(usuario_encontrado[5])
                                        break
                                    else:
                                        if usuario_encontrado[5] != no_recibieron_comida[semana_numero - 1][i]:
                                            no_recibieron_comida[semana_numero - 1][i] = usuario_encontrado[5]
                                            break
                                print("La comida se ha asignado a un aprendiz de la segunda semana.")
                            else:
                                print("Opción no válida.")
                    else:
                        intentos += 1
                        print(f"Credenciales incorrectas. Intento {intentos} de {intentos_maximos}")

                        # Si se alcanzan los intentos máximos, bloquear la cuenta
                        if intentos == intentos_maximos:
                            print("Ha excedido el número de intentos permitidos.")
                            # Eliminar al usuario de la lista de aprendices registrados
                            if usuario_encontrado:
                                usuarios_registrados.remove(usuario_encontrado)  
                                
                            # Agregar al usuario a la lista de bloqueados
                            usuarios_bloqueados.append(usuario_encontrado)
                            print(f"Usuario {usuario_encontrado[0]} bloqueado.")

                else:
                    print("Usuario no encontrado. Regístrese primero.")

                if opcion_aprendiz == "3":
                    # Código para recuperar cuenta
                    print("Recuperación de cuenta no disponible en esta versión.")
                    break

                elif opcion_aprendiz == "4":
                    print("Saliendo...")
                    break
            elif opcion_aprendiz == "3":
                print("Para recuperar su cuenta necesita:")
                numero_documento = input("Ingrese su número de documento: ")

                usuario_encontrado = None
                index = 0
                while index < len(usuarios_registrados):
                    if usuarios_registrados[index][2] == numero_documento:  # Cedula es el tercer elemento
                        usuario_encontrado = usuarios_registrados[index]
                        break
                    index += 1

                if usuario_encontrado:
                    nombre = usuario_encontrado[0]
                    print(f"Bienvenido {nombre}")
                    print(f"Su contraseña es: {usuario_encontrado[6]}")
                    decision = input("Desea cambiar la contraseña (si/no): ")
                    if decision.lower() == "si":
                        nueva_contraseña = input("Ingrese la nueva contraseña: ")
                        confirmar_contraseña = input("Confirme la nueva contraseña: ")

                        if nueva_contraseña == confirmar_contraseña:
                            usuario_encontrado[6] = nueva_contraseña  # Cambiar la contraseña en la lista
                            print("Contraseña cambiada exitosamente.")
                        else:
                            print("Las contraseñas no coinciden. No se realizó ningún cambio.")
                    else:
                        print("Regrese pronto.")
                else:
                    print("Usuario no encontrado.")
            elif opcion_aprendiz == "4":
                print("Saliendo del sistema. ¡Hasta pronto!")
                break        
    elif seleccion == "2":  # Opción para el Administrador
        usuario_admin = input("Ingrese su usuario administrador: ")
        contras_admin = input("Ingrese su contraseña administrador: ")

        if usuario_admin == usu_admin and contra_admin == contras_admin:
            while True:
                print("           BIENVENIDO ADMINISTRADOR")
                print("")
                print("        SU INICIO DE SESION FUE EXITOSO.")
                print("")
                print("      ____________________________________________")
                print("     |    ESTA SON LAS OPCIONES DEL ADMINISTRADOR |")
                print("     |____________________________________________|")
                print("    ________________________________________________")
                print("1: | Registrar aprendices                           |")
                print("2: | Eliminar usuarios                              |")
                print("3: | Actualizar datos y credenciales de acceso      |")
                print("4: | Desbloquear usuario por ingreso erróneo        |")
                print("5: | Actualización de Menú                          |")
                print("6: | Reasignación de semanas                        |")
                print("7: | Generar reporte mensual                        |")
                print("8: | Salir                                          |")
                print("   |________________________________________________|")
                opcion_admin = input("Ingrese la opción deseada: ")

                if opcion_admin == "1":
                    # Registro de nuevos aprendices por administrador
                    while True:
                        nombre = input("Ingrese el nombre del aprendiz: ")
                        valido = True
                        for char in nombre:
                            if char.isdigit():
                                valido = False
                                break
                        if valido:
                            break
                    while True:
                        apellido = input("Ingrese el apellido del aprendiz: ")
                        valido = True
                        for char in apellido:
                            if char.isdigit():
                                valido = False
                                break
                        if valido:
                            break

                    while True:
                        cedula = input("Ingrese la cédula del aprendiz: ")
                        if cedula.isdigit() and 8 <= len(cedula) <= 10:
                            break
                        else:
                            print("La cédula debe contener entre 8 y 10 dígitos Y no puede contener letras. Inténtelo de nuevo.")

                    print("Seleccione el programa de formación:")
                    print("------------------------------")
                    for programa in programas:
                        print(f"{programa[0]}. {programa[1]}")
                    print("------------------------------")
                    programa_numero = int(input("Ingrese el número del programa de formación: "))
                    programa_nombre = "Desconocido"
                    for programa in programas:
                        if programa[0] == programa_numero:
                            programa_nombre = programa[1]
                            break

                    semana = f"Semana ({(programa_numero - 1) // 2 + 1})"

                    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                    dominios_permitidos = ['gmail.com', 'hotmail.com', 'yahoo.com']

                    while True:
                        correo_electronico = input("Ingrese el correo electrónico del aprendiz: ").strip()
                        if re.match(patron_correo, correo_electronico):
                            dominio = correo_electronico.split('@')[1]
                            if dominio in dominios_permitidos:
                                print("Correo electrónico válido. Acceso permitido.")
                                break
                            else:
                                print("Lo siento, el dominio de correo electrónico no está permitido.")
                        else:
                            print("Formato de correo electrónico inválido. Por favor, inténtelo de nuevo.")

                    # Generar usuario único
                    usuario_base = nombre[0].lower() + apellido.lower()
                    usuario = usuario_base
                    contador = 1
                    while any(user[5] == usuario for user in usuarios_registrados):
                        usuario += random.choice(caracteres_especiales)
                        contador += 1

                    # Generar contraseña aleatoria
                    numero_clave = random.randint(1000, 9999)
                    letra = random.choice(string.ascii_uppercase)
                    clave = f"{letra}{numero_clave:04d}{nombre}"

                    # Mostrar datos generados
                    print("---------------------------------")
                    print(f"Usuario generado: {usuario}")
                    print(f"Clave generada: {clave}")

                    # Guardar usuario en la lista de usuarios registrados
                    nuevo_usuario = [
                        nombre, apellido, cedula, programa_nombre, correo_electronico, usuario, clave, semana
                    ]
                    usuarios_registrados.append(nuevo_usuario)

                    print("")
                    print("   EL REGISTRO FUE EXITOSO ")
                    print("")
                    print("       INICIAR SESION ")

                elif opcion_admin == "2":
                    usuario_a_eliminar = input("Ingrese el usuario del aprendiz a eliminar: ")
                    usuario_encontrado = None
                    for user in usuarios_registrados:
                        if user[5] == usuario_a_eliminar:
                            usuario_encontrado = user
                            break
                    if usuario_encontrado:
                        usuarios_registrados.remove(usuario_encontrado)
                        print(f"El usuario {usuario_a_eliminar} ha sido eliminado.")
                    else:
                        print("Usuario no encontrado.")
                    print("")

                elif opcion_admin == "3":
                    print("Lista de usuarios registrados:")
                    for user in usuarios_registrados:
                        print(user[5])  # 'usuario' está en la posición 5 de la lista
                    
                    usuario_actualizar = input("Ingrese el nombre de usuario a actualizar: ")
                    usuario_encontrado = None
                    for user in usuarios_registrados:
                        if user[5] == usuario_actualizar:  # 'usuario' está en la posición 5 de la lista
                            usuario_encontrado = user
                            break

                    if usuario_encontrado:
                        print("Seleccione qué desea actualizar:")
                        print("1. Nombre")
                        print("2. Apellido")
                        print("3. Cédula")
                        print("4. Programa de formación")
                        print("5. Contraseña")
                        print("6. Correo electrónico")

                        opcion_actualizar = input("Ingrese el número de la opción a actualizar: ")

                        if opcion_actualizar == "1":
                            nuevo_nombre = input("Ingrese el nuevo nombre: ")
                            usuario_encontrado[0] = nuevo_nombre  # 'nombre' está en la posición 0 de la lista
                            print("Nombre actualizado exitosamente.")
                        elif opcion_actualizar == "2":
                            nuevo_apellido = input("Ingrese el nuevo apellido: ")
                            usuario_encontrado[1] = nuevo_apellido  # 'apellido' está en la posición 1 de la lista
                            print("Apellido actualizado exitosamente.")
                        elif opcion_actualizar == "3":
                            nueva_cedula = input("Ingrese la nueva cédula: ")
                            usuario_encontrado[2] = nueva_cedula  # 'cedula' está en la posición 2 de la lista
                            print("Cédula actualizada exitosamente.")
                        elif opcion_actualizar == "4":
                            print("1. ADSO")
                            print("2. GESTION ADMINISTRATIVA")
                            print("3. GESTION EMPRESARIAL")
                            print("4. ANIMACION 3D")
                            print("5. MULTIMEDIA")
                            print("6. MODISTERIA")
                            print("7. COCINA")
                            print("8. GANADERIA")
                            nuevo_programa = input("Ingrese el número del nuevo programa: ")
                            programas = ["ADSO", "GESTION ADMINISTRATIVA", "GESTION EMPRESARIAL", "ANIMACION 3D", "MULTIMEDIA", "MODISTERIA", "COCINA", "GANADERIA"]
                            if nuevo_programa.isdigit() and 1 <= int(nuevo_programa) <= len(programas):
                                semana = f"Semana ({(int(nuevo_programa) - 1) // 2 + 1})"
                                usuario_encontrado[3] = programas[int(nuevo_programa) - 1]  # 'programa' está en la posición 3 de la lista
                                print(f"Programa actualizado a: {usuario_encontrado[3]}")
                                usuario_encontrado[6] = semana  # 'semana_alimentacion' está en la posición 6 de la lista
                            else:
                                print("Programa no válido.")
                        elif opcion_actualizar == "5":
                            numero_clave = random.randint(1000, 9999)
                            letra = random.choice(string.ascii_uppercase)
                            nueva_clave = f"{letra}{numero_clave:04d}{usuario_encontrado[0]}"  # 'nombre' está en la posición 0 de la lista
                            usuario_encontrado[4] = nueva_clave  # 'clave' está en la posición 4 de la lista
                            print(f"Nueva clave generada: {nueva_clave}")
                        elif opcion_actualizar == "6":
                            patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                            dominios_permitidos = ['gmail.com', 'hotmail.com', 'yahoo.com']
                            while True:
                                nuevo_correo = input("Ingrese el nuevo correo electrónico: ").strip()
                                if re.match(patron_correo, nuevo_correo):
                                    dominio = nuevo_correo.split('@')[1]
                                    if dominio in dominios_permitidos:
                                        usuario_encontrado[7] = nuevo_correo  # 'correo' está en la posición 7 de la lista
                                        print("Correo electrónico actualizado exitosamente.")
                                        break
                                    else:
                                        print("Lo siento, el dominio de correo electrónico no está permitido.")
                                else:
                                    print("Formato de correo electrónico inválido. Por favor, inténtalo de nuevo.")
                        else:
                            print("Opción inválida.")
                    else:
                        print("Usuario no encontrado.")

                elif opcion_admin == "4":
                    usuario_a_desbloquear = input("Ingrese el usuario del aprendiz a desbloquear: ")
                    usuario_encontrado = None
                    
                    # Buscar el usuario en la lista de bloqueados
                    for usuario_encontrado in usuarios_bloqueados:
                        if usuario_encontrado[0] == usuario_a_desbloquear:
                            usuario = usuario_encontrado
                            break

                    if usuario_encontrado:
                        usuarios_bloqueados.remove(usuario_encontrado)
                        usuarios_registrados.append(usuario_encontrado)
                        print(f"El usuario {usuario_a_desbloquear} ha sido desbloqueado y agregado nuevamente a la lista de aprendices registrados.")
                    else:
                        print("Usuario no encontrado en la lista de bloqueados.")
                    print("")

                elif opcion_admin == "5":
                    print("Actualización de Menú:")
                    
                    # Definir el menú actual en formato de listas (cada día de la semana como una lista de opciones)
                    menu_semanal = [
                        ["Lunes     = Arroz de pollo y ensalada."],
                        ["Martes    = Arroz con carne y ensalada."],
                        ["Miércoles = Arroz con carne molida y papas fritas."],
                        ["Jueves    = Arroz con cerdo y ensalada."],
                        ["Viernes   = Arroz con pescado frito."]
                    ]
                    
                    # Mostrar el menú actual
                    print("Menú actual:")
                    for dia in menu_semanal:
                        print(dia[0])
                    
                    print("\nSeleccione el día del menú a actualizar:")
                    print("1. Lunes")
                    print("2. Martes")
                    print("3. Miércoles")
                    print("4. Jueves")
                    print("5. Viernes")
                    
                    opcion_actualizar_menu = input("Ingrese el número del día a actualizar: ")
                    
                    if opcion_actualizar_menu == "1":
                        nuevo_menu = input("Ingrese el nuevo menú para el Lunes: ")
                        menu_semanal[0][0] = f"Lunes     = {nuevo_menu}"
                        print("Menú del Lunes actualizado exitosamente.")
                    elif opcion_actualizar_menu == "2":
                        nuevo_menu = input("Ingrese el nuevo menú para el Martes: ")
                        menu_semanal[1][0] = f"Martes    = {nuevo_menu}"
                        print("Menú del Martes actualizado exitosamente.")
                    elif opcion_actualizar_menu == "3":
                        nuevo_menu = input("Ingrese el nuevo menú para el Miércoles: ")
                        menu_semanal[2][0] = f"Miércoles = {nuevo_menu}"
                        print("Menú del Miércoles actualizado exitosamente.")
                    elif opcion_actualizar_menu == "4":
                        nuevo_menu = input("Ingrese el nuevo menú para el Jueves: ")
                        menu_semanal[3][0] = f"Jueves    = {nuevo_menu}"
                        print("Menú del Jueves actualizado exitosamente.")
                    elif opcion_actualizar_menu == "5":
                        nuevo_menu = input("Ingrese el nuevo menú para el Viernes: ")
                        menu_semanal[4][0] = f"Viernes   = {nuevo_menu}"
                        print("Menú del Viernes actualizado exitosamente.")
                    else:
                        print("Opción inválida.")
                    
                    # Mostrar el menú actualizado
                    print("\nMenú actualizado:")
                    for dia in menu_semanal:
                        print(dia[0])
                    
                    print("")

                elif opcion_admin == "6":
                    print("Reasignación en proceso")
                    import random

                    programas = [
                        "ADSO Y GESTION ADMINISTRATIVA",
                        "GESTION EMPRESARIAL Y ANIMACION 3D",
                        "MULTIMEDIA Y MODISTERIA",
                        "COCINA Y GANADERIA"
                    ]

                    random.shuffle(programas)

                    semanas = [1, 2, 3, 4]
                    print("")

                    for semana, programa in zip(semanas, programas):
                        print(f"Semana {semana}: alimentación para los programas de {programa}")
                        print("------------------------------------------------------------")
                        print("")

                elif opcion_admin == "7":
                    print("Generación de reporte mensual en proceso")
                    print("----------------------------------------------------")
                    print(" RACIONES TOTALES RECIBIDAS  ",contador_si )
                    print("----------------------------------------------------")
                    print("")
                    print(" RACIONES TOTALES NO RECIBIDAS  ", contador_no )
                    print("----------------------------------------------------")
                    print("Fin del reporte mensual")
                    print("")


                elif opcion_admin == "8":
                    print("Saliendo...")
                    break

                else:
                    print("Opción no válida. Inténtelo de nuevo.")                
    elif seleccion == "3":  
        nombre_invitado = input("ingrese su nombre ")
        
        print("Bienvenido Invitado",nombre_invitado," ahora solo podra visualizar imformacion")
        print("")
        print("  ESTOS SON LOS PROGRAMAS BENEFICIADOS  ")
        print(" _____________________________________ ")
        print("|                ADSO                 |")
        print("|        GESTION ADMINISTRATIVA       | ")
        print("|         GESTION EMPRESARIAL         |")
        print("|            ANIMACION 3D             |")
        print("|             MULTIMEDIA              |")
        print("|             MODISTERIA              |")
        print("|               COCINA                |")
        print("|              GANADERIA              |")
        print("|_____________________________________|")
        print("")
        print("      SEMANAS DE ALIMENTACION ASIGNADAS PARA LOS PROGRAMAS :")
        print("")
        print("")
        print("Semana 1: alimentacion para el programa de ADSO, GESTION ADMINISTRATIVA")
        print("Semana 2: alimentacion para el programa de GESTION EMPRESARIAL, ANIMACION 3D")
        print("Semana 3: alimentacion para el programa de MULTIMEDIA, MODISTERIA")
        print("Semana 4: alimentacion para el programa de COCINA, GANADERIA")
        print("")
        


        
        print("")
        print("  ACONTINUACION SE LE MOSTRARA EL MENU DE LA SEMANA .")
        print("               MENU DE LA SEMANA   ")
        print("")
        print(" ______________________________________________________")
        print("| Lunes     = Arroz de pollo y ensalda.                |" )
        print("| Martes    = Arroz con carne y ensalada.              |" )
        print("| Miércoles = Arroz con carne molida y papas fritas.   |" )
        print("| Jueves    = Arroz con cerdo y ensalada.              |" )
        print("| Viernes   = Arroz con pescado frito.                 |" )
        print("|______________________________________________________|")
        print("")
    elif seleccion == "4":
        print(" ______________________________________________________")  
        print("|     GRACIAS POR UTILIZAR EL PROGRAMA, VUELVE PRONTO .|")
        print("|______________________________________________________|")
        break


    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")