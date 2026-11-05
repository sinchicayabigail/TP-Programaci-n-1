from validaciones.validaciones import validar_numero


def seleccionar_tabla(tablas, cantidad_tablas):
    '''
    Permite elegir una tabla de las disponibles.
    '''

    posicion = -1

    if cantidad_tablas == 0:
        print("Todavía no hay tablas creadas.")
    else:
        print("Tablas disponibles")

        for i in range(cantidad_tablas):
            print(i + 1, tablas[i][0])

        opcion = input("Seleccione una tabla")

        while not validar_numero(opcion) or int(opcion) < 1 or int(opcion) > cantidad_tablas:
            print("La opción no es válida.")
            opcion = input("Seleccione una tabla")

        posicion = int(opcion) - 1

    return posicion

def mostrar_tabla(tabla):
    '''
    Muestra todos los datos de una tabla.
    '''

    print()
    print("Tabla", tabla[0])

    encabezado = ""

    for j in range(tabla[5]):
        encabezado = encabezado + tabla[1][j] + "-"

    print(encabezado)

    for i in range(tabla[4]):
        fila = ""

        for j in range(tabla[5]):
            fila = fila + str(tabla[3][i][j]) + "-"

        print(fila)

def mostrar_fila(tabla):
    '''
    Permite seleccionar y mostrar una fila.
    '''

    fila = input("Ingrese el número de fila")

    while not validar_numero(fila) or int(fila) < 1 or int(fila) > tabla[4]:
        print("La fila no es válida.")
        fila = input("Ingrese el número de fila")

    fila = int(fila) - 1

    if tabla[2][fila] == None:
        print("Fila", fila + 1)
    else:
        print(tabla[2][fila])

    for j in range(tabla[5]):
        print(tabla[1][j])
        print(tabla[3][fila][j])


def mostrar_columna(tabla):
    '''
    Permite seleccionar y mostrar una columna.
    '''

    columna = input("Ingrese el número de columna")

    while not validar_numero(columna) or int(columna) < 1 or int(columna) > tabla[5]:
        print("La columna no es válida.")
        columna = input("Ingrese el número de columna")

    columna = int(columna) - 1

    print(tabla[1][columna])

    for i in range(tabla[4]):
        if tabla[2][i] == None:
            print("Fila", i + 1)
        else:
            print(tabla[2][i])

        print(tabla[3][i][columna])



def seleccionar_columnas(tabla):
    '''
    Permite elegir qué columnas se desean mostrar.
    '''

    columnas_elegidas = [None] * tabla[5]

    print("Columnas disponibles")

    for i in range(tabla[5]):
        print(i + 1, tabla[1][i])

    cantidad = input("Cuántas columnas desea mostrar")

    while not validar_numero(cantidad) or int(cantidad) < 1 or int(cantidad) > tabla[5]:
        print("La cantidad no es válida.")
        cantidad = input("Cuántas columnas desea mostrar")

    cantidad = int(cantidad)

    for i in range(cantidad):
        columna = input("Ingrese el número de columna")

        while not validar_numero(columna) or int(columna) < 1 or int(columna) > tabla[5]:
            print("La columna no es válida.")
            columna = input("Ingrese el número de columna")

        columnas_elegidas[i] = int(columna) - 1

    print("Resultado")

    for i in range(tabla[4]):
        if tabla[2][i] == None:
            print("Fila", i + 1)
        else:
            print(tabla[2][i])

        for j in range(cantidad):
            columna = columnas_elegidas[j]
            print(tabla[1][columna])
            print(tabla[3][i][columna])

    print("Resultado")

    for i in range(tabla[4]):
        if tabla[2][i] == None:
            print("Fila", i + 1)
        else:
            print(tabla[2][i])

        for j in range(cantidad):
            columna = columnas_elegidas[j]
            print(tabla[1][columna])
            print(tabla[3][i][columna])


def filtrar_tabla(tabla):
    '''
    Busca datos específicos dentro de una tabla.
    '''

    print("Columnas disponibles")

    for i in range(tabla[5]):
        print(i + 1, tabla[1][i])

    columna = input("Seleccione la columna para filtrar")

    while not validar_numero(columna) or int(columna) < 1 or int(columna) > tabla[5]:
        print("La columna no es válida.")
        columna = input("Seleccione la columna para filtrar")

    columna = int(columna) - 1
    valor = input("Ingrese el valor que desea buscar")

    print("Resultados")

    encontrados = 0

    for i in range(tabla[4]):
        if tabla[3][i][columna] == valor:
            encontrados += 1

            if tabla[2][i] == None:
                print("Fila", i + 1)
            else:
                print(tabla[2][i])

            for j in range(tabla[5]):
                print(tabla[1][j])
                print(tabla[3][i][j])

    if encontrados == 0:
        print("No se encontraron resultados.")


def gestionar_mostrar(tablas, cantidad_tablas):
    '''
    Muestra las opciones para visualizar y filtrar tablas.
    '''
    
    opcion = ""

    while opcion != "6":
        print("MOSTRAR INFORMACIÓN")
        print("1. Mostrar tabla completa")
        print("2. Mostrar una fila")
        print("3. Mostrar una columna")
        print("4. Seleccionar columnas")
        print("5. Filtrar tabla")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción")

        if opcion == "1":
            posicion = seleccionar_tabla(tablas, cantidad_tablas)

            if posicion != -1:
                mostrar_tabla(tablas[posicion])

        elif opcion == "2":
            posicion = seleccionar_tabla(tablas, cantidad_tablas)

            if posicion != -1:
                mostrar_fila(tablas[posicion])

        elif opcion == "3":
            posicion = seleccionar_tabla(tablas, cantidad_tablas)

            if posicion != -1:
                mostrar_columna(tablas[posicion])

        elif opcion == "4":
            posicion = seleccionar_tabla(tablas, cantidad_tablas)

            if posicion != -1:
                seleccionar_columnas(tablas[posicion])

        elif opcion == "5":
            posicion = seleccionar_tabla(tablas, cantidad_tablas)

            if posicion != -1:
                filtrar_tabla(tablas[posicion])

        elif opcion != "6":
            print("Opción incorrecta.")