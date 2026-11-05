from validaciones.validaciones import validar_numero


def seleccionar_tabla(tablas, cantidad_tablas):
    '''
    Permite elegir una tabla para realizar los cálculos.
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


def seleccionar_columna(tabla):
    '''
    Permite elegir una columna de la tabla.
    '''

    print("Columnas disponibles")

    for i in range(tabla[5]):
        print(i + 1, tabla[1][i])

    columna = input("Seleccione una columna")

    while not validar_numero(columna) or int(columna) < 1 or int(columna) > tabla[5]:
        print("La columna no es válida.")
        columna = input("Seleccione una columna")

    return int(columna) - 1


def obtener_datos_numericos(tabla, columna):
    '''
    Obtiene los valores numéricos de una columna.
    '''

    datos = [None] * tabla[4]
    cantidad = 0

    for i in range(tabla[4]):
        dato = tabla[3][i][columna]

        if validar_numero(dato):
            datos[cantidad] = int(dato)
            cantidad += 1

    return datos, cantidad


def ordenar_datos(datos, cantidad):
    '''
    Ordena los números de menor a mayor.
    '''

    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):
            if datos[j] > datos[j + 1]:
                auxiliar = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = auxiliar


def calcular_frecuencias(datos, cantidad):
    '''
    Calcula las frecuencias y la moda de los datos.
    '''

    valores = [None] * cantidad
    frecuencias = [0] * cantidad
    cantidad_valores = 0

    for i in range(cantidad):
        encontrado = False
        posicion = 0

        while posicion < cantidad_valores and encontrado == False:
            if valores[posicion] == datos[i]:
                encontrado = True
            else:
                posicion += 1

        if encontrado:
            frecuencias[posicion] += 1
        else:
            valores[cantidad_valores] = datos[i]
            frecuencias[cantidad_valores] = 1
            cantidad_valores += 1

    print("Frecuencias")

    for i in range(cantidad_valores):
        print(valores[i], frecuencias[i])

    mayor_frecuencia = 0

    for i in range(cantidad_valores):
        if frecuencias[i] > mayor_frecuencia:
            mayor_frecuencia = frecuencias[i]

    print("Moda")

    if mayor_frecuencia == 1:
        print("No hay moda.")
    else:
        for i in range(cantidad_valores):
            if frecuencias[i] == mayor_frecuencia:
                print(valores[i])


def calcular_maximo_minimo(datos, cantidad):
    '''
    Calcula el valor máximo y mínimo de los datos.
    '''

    mayor = datos[0]
    menor = datos[0]

    for i in range(1, cantidad):
        if datos[i] > mayor:
            mayor = datos[i]

        if datos[i] < menor:
            menor = datos[i]

    print("Valor máximo", mayor)
    print("Valor mínimo", menor)


def calcular_promedios(datos, cantidad):
    '''
    Calcula el promedio aritmético y geométrico.
    '''

    suma = 0
    producto = 1

    for i in range(cantidad):
        suma += datos[i]
        producto *= datos[i]

    promedio_aritmetico = suma / cantidad
    promedio_geometrico = producto ** (1 / cantidad)

    print("Promedio aritmético", promedio_aritmetico)
    print("Promedio geométrico", promedio_geometrico)


def calcular_diferencias(datos, cantidad):
    '''
    Calcula el resultado y el desvio.
    '''

    suma = 0

    for i in range(cantidad):
        suma += datos[i]

    promedio = suma / cantidad
    suma_diferencias = 0

    for i in range(cantidad):
        diferencia = datos[i] - promedio
        suma_diferencias += diferencia ** 2

    resultado = suma_diferencias / cantidad
    desvio = resultado ** 0.5

    print("Resultado", resultado)
    print("Desvio", desvio)


def calcular_posicion(datos, cantidad):
    ordenar_datos(datos, cantidad)
    '''
    Ordena los datos y calcula la mediana.
    '''

    if cantidad % 2 == 0:
        posicion = cantidad // 2
        mediana = (datos[posicion - 1] + datos[posicion]) / 2
    else:
        posicion = cantidad // 2
        mediana = datos[posicion]

    print("Mediana", mediana)

def gestionar_estadisticas(tablas, cantidad_tablas):
    '''
    Permite realizar los cálculos estadísticos de una tabla.
    '''
    
    posicion = seleccionar_tabla(tablas, cantidad_tablas)

    if posicion != -1:
        tabla = tablas[posicion]
        columna = seleccionar_columna(tabla)

        datos, cantidad = obtener_datos_numericos(tabla, columna)

        if cantidad == 0:
            print("La columna no contiene números enteros positivos o cero.")
        else:
            print("Cantidad de datos numéricos", cantidad)

            if cantidad < tabla[4]:
                print("Se ignoraron los datos que no son números enteros.")

            calcular_frecuencias(datos, cantidad)
            calcular_maximo_minimo(datos, cantidad)
            calcular_promedios(datos, cantidad)
            calcular_diferencias(datos, cantidad)
            calcular_posicion(datos, cantidad)