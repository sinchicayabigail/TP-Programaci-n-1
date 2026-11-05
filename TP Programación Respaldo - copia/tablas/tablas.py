from validaciones.validaciones import validar_numero


def ingresar_numero(mensaje, minimo, maximo):
    numero = input(mensaje)

    while not validar_numero(numero) or int(numero) < minimo or int(numero) > maximo:
        print("El número ingresado no es válido.")
        numero = input(mensaje)

    return int(numero)


def crear_matriz(cantidad_filas, cantidad_columnas):
    matriz = [None] * cantidad_filas

    for i in range(cantidad_filas):
        matriz[i] = [None] * cantidad_columnas

    return matriz


def crear_tabla(tablas, cantidad_tablas):
    if cantidad_tablas == 10:
        print("No se pueden crear más tablas.")
    else:
        nombre = input("Ingrese el nombre de la tabla")

        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Ingrese el nombre de la tabla")

        cantidad_filas = ingresar_numero(
            "Ingrese la cantidad de filas (1 a 20)", 1, 20
        )

        cantidad_columnas = ingresar_numero(
            "Ingrese la cantidad de columnas (1 a 10)", 1, 10
        )

        nombres_columnas = [None] * cantidad_columnas
        nombres_filas = [None] * cantidad_filas
        matriz = crear_matriz(cantidad_filas, cantidad_columnas)

        for i in range(cantidad_columnas):
            nombres_columnas[i] = input(
                "Ingrese el nombre de la columna " + str(i + 1)
            )

            while nombres_columnas[i] == "":
                print("El nombre no puede estar vacío.")
                nombres_columnas[i] = input(
                    "Ingrese el nombre de la columna " + str(i + 1)
                )

        respuesta = input("Desea asignar nombres a las filas (s/n)")

        if respuesta == "s" or respuesta == "S":
            for i in range(cantidad_filas):
                nombres_filas[i] = input(
                    "Ingrese el nombre de la fila " + str(i + 1)
                )

        print("Seleccione el tipo de carga")
        print("1. Secuencial (fila por fila)")
        print("2. Distribuida (columna por columna)")

        tipo_carga = ingresar_numero("Opción", 1, 2)

        if tipo_carga == 1:
            for i in range(cantidad_filas):
                print("Fila", i + 1)

                for j in range(cantidad_columnas):
                    matriz[i][j] = input(
                        "Ingrese el dato de " + nombres_columnas[j]
                    )
        else:
            for j in range(cantidad_columnas):
                print("Columna", nombres_columnas[j])

                for i in range(cantidad_filas):
                    matriz[i][j] = input(
                        "Ingrese el dato de la fila " + str(i + 1)
                    )

        tablas[cantidad_tablas] = [
            nombre,
            nombres_columnas,
            nombres_filas,
            matriz,
            cantidad_filas,
            cantidad_columnas
        ]

        cantidad_tablas += 1
        print("La tabla se creó correctamente.")

    return cantidad_tablas

def mostrar_tabla(tabla):
    print("Tabla", tabla[0])

    for i in range(tabla[4]):
        for j in range(tabla[5]):
            print(tabla[1][j], tabla[3][i][j])

def seleccionar_tabla(tablas, cantidad_tablas):
    posicion = -1

    if cantidad_tablas == 0:
        print("Todavía no hay tablas creadas.")
    else:
        print("Tablas disponibles")

        for i in range(cantidad_tablas):
            print(i + 1, tablas[i][0])

        opcion = ingresar_numero(
            "Seleccione una tabla", 1, cantidad_tablas
        )

        posicion = opcion - 1

    return posicion


def modificar_fila(tabla):
    fila = ingresar_numero(
        "Ingrese el número de fila que desea modificar",
        1,
        tabla[4]
    )

    fila -= 1

    for j in range(tabla[5]):
        print("Ingrese el nuevo dato de", tabla[1][j])
        tabla[3][fila][j] = input()

    if tabla[2][fila] != None:
        tabla[2][fila] = input("Ingrese el nuevo nombre de la fila")


def modificar_columna(tabla):
    columna = ingresar_numero(
        "Ingrese el número de columna que desea modificar",
        1,
        tabla[5]
    )

    columna -= 1

    for i in range(tabla[4]):
        print("Ingrese el nuevo dato de la fila", i + 1)
        tabla[3][i][columna] = input()

    respuesta = input("Desea cambiar el nombre de la columna (s/n)")

    if respuesta == "s" or respuesta == "S":
        nombre = input("Ingrese el nuevo nombre")

        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Ingrese el nuevo nombre")

        tabla[1][columna] = nombre


def gestionar_tablas(tablas, cantidad_tablas):
    opcion = ""

    while opcion != "4":
        print()
        print("GESTIÓN DE TABLAS")
        print("1. Crear tabla")
        print("2. Mostrar una tabla")
        print("3. Modificar una tabla")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción")

        if opcion == "1":
            cantidad_tablas = crear_tabla(tablas, cantidad_tablas)

        elif opcion == "2":
            posicion = seleccionar_tabla(tablas, cantidad_tablas)

            if posicion != -1:
                mostrar_tabla(tablas[posicion])

        elif opcion == "3":
            posicion = seleccionar_tabla(tablas, cantidad_tablas)

            if posicion != -1:
                print("¿Qué desea modificar?")
                print("1. Una fila")
                print("2. Una columna")

                modificacion = ingresar_numero("Opción", 1, 2)

                if modificacion == 1:
                    modificar_fila(tablas[posicion])
                else:
                    modificar_columna(tablas[posicion])

                print("La tabla se modificó correctamente.")

        elif opcion != "4":
            print("Opción incorrecta.")

    return cantidad_tablas