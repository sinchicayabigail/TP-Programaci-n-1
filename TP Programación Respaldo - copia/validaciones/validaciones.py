def validar_numero(cadena: str) -> bool:
    '''
    Verifica si el texto ingresado contiene solamente números.
    '''

    i = 0
    es_numero = True

    if cadena == "":
        es_numero = False

    while i < len(cadena) and es_numero:

        if ord(cadena[i]) < 48 or ord(cadena[i]) > 57:
            es_numero = False

        i += 1

    return es_numero


def validar_decimal(cadena: str) -> bool:
    '''
    Verifica si el texto contiene solamente dígitos.
    '''
    
    i = 0
    es_decimal = True
    cantidad_digitos = 0

    if cadena == "":
        es_decimal = False

    while i < len(cadena) and es_decimal:
        if ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57:
            cantidad_digitos += 1
        else:
            es_decimal = False

        i += 1

    if cantidad_digitos == 0:
        es_decimal = False

    return es_decimal


def validar_rango(valor: int, minimo: int, maximo: int) -> bool:
    '''
    Comprueba si un número se encuentra dentro de un rango.
    '''

    if valor >= minimo and valor <= maximo:
        return True
    else:
        return False


def es_par(numero: int) -> bool:
    '''
    Verifica si un número es par.
    '''

    if numero % 2 == 0:
        return True
    else:
        return False


def es_primo(numero: int, divisor: int = 2) -> bool:
    '''
    Comprueba si un número es primo mediante recursividad.
    '''

    if numero <= 1:
        return False

    elif divisor == numero:
        return True

    elif numero % divisor == 0:
        return False

    else:
        return es_primo(numero, divisor + 1)


def es_multiplo(numero: int, otro_numero: int) -> bool:
    '''
    Verifica si un número es múltiplo de otro.
    '''

    if otro_numero == 0:
        return False

    elif numero % otro_numero == 0:
        return True

    else:
        return False