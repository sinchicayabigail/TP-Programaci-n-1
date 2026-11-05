from variables.variables import gestionar_variables
from validaciones.validaciones import validar_numero
from tablas.tablas import gestionar_tablas
from mostrar.mostrar import gestionar_mostrar
from estadisticas.estadisticas import gestionar_estadisticas

usuario = "soluno"
contrasena = "777"

nombre_usuario = input("Ingrese su nombre de usuario: ")

registro_nuevo = False
acceso = False

while nombre_usuario == "":
    print("El nombre de usuario no puede estar vacio.")
    nombre_usuario = input("Ingrese su nombre de usuario: ")

while nombre_usuario != usuario:

    print("El nombre de usuario no esta registrado.")

    registro = input("Desea registrarse Si o No: ")

    while registro != "Si" and registro != "No":
        print("Ingrese Si o No.")
        registro = input("Desea registrarse Si o No: ")

    if registro == "Si":

        usuario = nombre_usuario

        print("Usuario registrado correctamente.")

        contrasena = input("Ingrese una contraseña: ")

        while contrasena == "":
            print("La contraseña no puede estar vacia.")
            contrasena = input("Ingrese una contraseña: ")

        registro_nuevo = True
        acceso = True

    else:

        nombre_usuario = input("Ingrese un nombre de usuario valido: ")

        while nombre_usuario == "":
            print("El nombre no puede estar vacio.")
            nombre_usuario = input("Ingrese un nombre de usuario: ")


if registro_nuevo == False:

    contador = 0

    while contador < 3 and acceso == False:

        contrasena_usuario = input("Ingrese la contraseña: ")

        if contrasena_usuario == contrasena:

            print("Acceso concedido.")
            acceso = True

        else:

            print("La contraseña es incorrecta.")
            contador += 1

    if acceso == False:
        print("Se agotaron los intentos.")


proyectos = ["Proyecto 1", "Proyecto 2", "Proyecto 3"]
proyecto_activo = ""

tablas = [None] * 10
cantidad_tablas = 0

nombres_variables = [None] * 10
tipos_variables = [None] * 10
valores_variables = [None] * 10

cantidad_variables = 0


if acceso == True:

    continuar = True

    while continuar:

        print()
        print("===== MENU PRINCIPAL =====")
        print("a) Proyectos")
        print("b) Tablas")
        print("c) Variables")
        print("d) Mostrar")
        print("e) Estadistica")
        print("f) Salir")
        print("==========================")

        opcion = input("Ingrese una opcion: ")

        if opcion == "a":

            print("Proyectos disponibles:")

            for i in range(len(proyectos)):
                print(i + 1, proyectos[i])

            seleccion = input("Seleccione un proyecto: ")

            while not validar_numero(seleccion) or int(seleccion) < 1 or int(seleccion) > len(proyectos):
                print("Proyecto incorrecto.")
                seleccion = input("Seleccione un proyecto: ")

            proyecto_activo = proyectos[int(seleccion) - 1]

            print("Proyecto seleccionado:", proyecto_activo)

        elif opcion == "b":

            cantidad_tablas = gestionar_tablas(tablas, cantidad_tablas)

        elif opcion == "c":

            cantidad_variables = gestionar_variables(
                nombres_variables,
                tipos_variables,
                valores_variables,
                cantidad_variables
            )

        elif opcion == "d":

            gestionar_mostrar(tablas, cantidad_tablas)

        elif opcion == "e":

            gestionar_estadisticas(tablas, cantidad_tablas)

        elif opcion == "f":

            print("Programa finalizado.")
            continuar = False

        else:

            print("Opcion incorrecta.")

else:

    print("No se pudo ingresar al sistema.")