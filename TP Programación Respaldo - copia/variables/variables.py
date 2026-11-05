from validaciones.validaciones import validar_numero, validar_decimal


def crear_variable(nombres, tipos, valores, cantidad):

    if cantidad < 100:

        nombre = input("Ingrese el nombre de la variable: ")

        while nombre == "":
            print("El nombre no puede estar vacio.")
            nombre = input("Ingrese el nombre de la variable: ")

        encontrado = True

        while encontrado:

            encontrado = False

            for i in range(cantidad):
                if nombres[i] == nombre:
                    encontrado = True

            if encontrado:
                print("Esa variable ya existe.")
                nombre = input("Ingrese otro nombre: ")

                while nombre == "":
                    print("El nombre no puede estar vacio.")
                    nombre = input("Ingrese otro nombre: ")

        print("1. Entero")
        print("2. Decimal")
        print("3. Texto")

        tipo = input("Seleccione el tipo: ")

        while tipo != "1" and tipo != "2" and tipo != "3":
            print("Tipo incorrecto.")
            tipo = input("Seleccione el tipo: ")

        if tipo == "1":
            tipo = "Entero"

        elif tipo == "2":
            tipo = "Decimal"

        else:
            tipo = "Texto"

        nombres[cantidad] = nombre
        tipos[cantidad] = tipo
        valores[cantidad] = "Sin cargar"

        cantidad += 1

        print("Variable creada correctamente.")

    else:
        print("Se alcanzo el limite de variables.")

    return cantidad


def mostrar_variables(nombres, tipos, valores, cantidad):

    if cantidad == 0:

        print("No hay variables creadas.")

    else:

        print("Variables creadas")

        for i in range(cantidad):
            print("Nombre", nombres[i])
            print("Tipo", tipos[i])
            print("Valor", valores[i])
            print()


def seleccionar_variable(nombres, tipos, valores, cantidad):

    posicion = -1

    if cantidad == 0:

        print("No hay variables creadas.")

    else:

        for i in range(cantidad):
            print(i + 1, nombres[i], tipos[i], valores[i])

        numero = input("Seleccione el numero de la variable: ")

        while validar_numero(numero) == False:
            print("Debe ingresar un numero.")
            numero = input("Seleccione el numero de la variable: ")

        numero = int(numero)

        while numero < 1 or numero > cantidad:

            print("Numero incorrecto.")
            numero = input("Seleccione un numero valido: ")

            while validar_numero(numero) == False:
                print("Debe ingresar un numero.")
                numero = input("Seleccione un numero valido: ")

            numero = int(numero)

        posicion = numero - 1

    return posicion


def modificar_variable(nombres, tipos, valores, cantidad):

    posicion = seleccionar_variable(nombres, tipos, valores, cantidad)

    if posicion != -1:

        if tipos[posicion] == "Entero":

            valor = input("Ingrese el nuevo valor entero: ")

            while validar_numero(valor) == False:
                print("Ingrese un numero entero positivo.")
                valor = input("Ingrese el nuevo valor entero: ")

            valores[posicion] = int(valor)

        elif tipos[posicion] == "Decimal":

            valor = input("Ingrese el nuevo valor decimal: ")

            while validar_decimal(valor) == False:
                print("Ingrese un numero decimal valido.")
                valor = input("Ingrese el nuevo valor decimal: ")

            valores[posicion] = float(valor)

        else:

            valor = input("Ingrese el nuevo valor de texto: ")
            valores[posicion] = valor

        print("Variable modificada correctamente.")


def gestionar_variables(nombres, tipos, valores, cantidad):

    continuar = True

    while continuar:

        print("===== GESTION DE VARIABLES =====")
        print("1. Crear variable")
        print("2. Mostrar variables")
        print("3. Modificar variable")
        print("4. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            cantidad = crear_variable(nombres, tipos, valores, cantidad)

        elif opcion == "2":

            mostrar_variables(nombres, tipos, valores, cantidad)

        elif opcion == "3":

            modificar_variable(nombres, tipos, valores, cantidad)

        elif opcion == "4":

            continuar = False

        else:

            print("Opcion incorrecta.")

    return cantidad