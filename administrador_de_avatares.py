ids = []
avatares = []
propietarios = []
clases = []
niveles = []
experiencias = []
razas = []
estados = []
observaciones = []
#-------------------------------------------#
#--|menu_principal_administrador_avatares|--#
#-------------------------------------------#
while True:
    print("menu principal administrador de avatares")
    print("1) crear avatar")
    print("2) editar avatar")
    print("3) eliminar avatar")
    print("4) buscar avatar")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #------------------#
    #--|crear_avatar|--#
    #------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_avatar = 1
        else:
            id_avatar = ids[-1] + 1
        avatar = input("nombre del avatar: ")
        propietario = input("nombre del propietario: ")
        clase = input("clase del avatar: ")
        nivel = int(input("nivel: "))
        experiencia = int(input("experiencia: "))
        raza = input("raza: ")
        estado = input("estado del avatar: ")
        observacion = input("observación: ")
        ids.append(id_avatar)
        avatares.append(avatar)
        propietarios.append(propietario)
        clases.append(clase)
        niveles.append(nivel)
        experiencias.append(experiencia)
        razas.append(raza)
        estados.append(estado)
        observaciones.append(observacion)
        print("avatar registrado correctamente.")
        print("id:", id_avatar)
    #-------------------#
    #--|editar_avatar|--#
    #-------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar avatar")
            for i in range(len(ids)):
                print(f"{ids[i]} | {avatares[i]} | {propietarios[i]} | {clases[i]} | {niveles[i]} | {experiencias[i]} | {razas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {avatares[posicion]} | {propietarios[posicion]} | {clases[posicion]} | {niveles[posicion]} | {experiencias[posicion]} | {razas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                avatares[posicion] = input("nuevo nombre del avatar: ")
                propietarios[posicion] = input("nuevo propietario: ")
                clases[posicion] = input("nueva clase: ")
                niveles[posicion] = int(input("nuevo nivel: "))
                experiencias[posicion] = int(input("nueva experiencia: "))
                razas[posicion] = input("nueva raza: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|eliminar_avatar|--#
    #---------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar avatar")
            for i in range(len(ids)):
                print(f"{ids[i]} | {avatares[i]} | {propietarios[i]} | {clases[i]} | {niveles[i]} | {experiencias[i]} | {razas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {avatares[posicion]} | {propietarios[posicion]} | {clases[posicion]} | {niveles[posicion]} | {experiencias[posicion]} | {razas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    avatares.pop(posicion)
                    propietarios.pop(posicion)
                    clases.pop(posicion)
                    niveles.pop(posicion)
                    experiencias.pop(posicion)
                    razas.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #-------------------#
    #--|buscar_avatar|--#
    #-------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar avatar")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {avatares[posicion]} | {propietarios[posicion]} | {clases[posicion]} | {niveles[posicion]} | {experiencias[posicion]} | {razas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma = 0
            mayor = niveles[0]
            menor = niveles[0]
            activos = 0
            inactivos = 0
            suspendidos = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {avatares[i]} | {propietarios[i]} | {clases[i]} | {niveles[i]} | {experiencias[i]} | {razas[i]} | {estados[i]} | {observaciones[i]}")
                suma += experiencias[i]
                if niveles[i] > mayor:
                    mayor = niveles[i]
                if niveles[i] < menor:
                    menor = niveles[i]
                if estados[i].lower() == "activo":
                    activos += 1
                elif estados[i].lower() == "inactivo":
                    inactivos += 1
                elif estados[i].lower() == "suspendido":
                    suspendidos += 1
            promedio = suma / len(ids)
            print("estadísticas administrador de avatares")
            print("cantidad de registros:", len(ids))
            print("experiencia acumulada:", suma)
            print("promedio de experiencia:", round(promedio, 2))
            print("mayor nivel:", mayor)
            print("menor nivel:", menor)
            print("avatares activos:", activos)
            print("avatares inactivos:", inactivos)
            print("avatares suspendidos:", suspendidos)
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el programa.")
        break
    else:
        print("opción inválida.")