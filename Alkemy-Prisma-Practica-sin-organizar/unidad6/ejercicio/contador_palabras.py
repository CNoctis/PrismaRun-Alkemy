def calculadora_letras(lista_palabras: list) -> list:
    """
    Calcula la cantidad de letras que posea una palabra
    lista_palabras: Lista de las palabras a calcular su logitud
    return: Lista con la cantidad de letras que contiene cada palabra
    """
    # Registro de la logitud de las palabras
    cantidad_letras = []

    for palabras in lista_palabras:
        cantidad_letras.append(len(palabras))

    return cantidad_letras


def calculadora_letras_dict(lista_palabras: list) -> dict:
    """Calcula la cantidad de letras que posea una palabra
    lista_palabras: Lista de las palabras a calcular su logitud
    return: Diccionario en relación clave-valor con respecto a su longitud
    """
    # Palabras y su longitud vinculada
    dict_palabra = {}

    for palabras in lista_palabras:
        dict_palabra[palabras] = len(palabras)
    return dict_palabra


def main():
    lista_palabras = ['perro', 'elefante', 'dragón']

    # Lista
    cantidad_letras = calculadora_letras(lista_palabras)
    print(cantidad_letras)

    # Diccionario
    dict_palabra = calculadora_letras_dict(lista_palabras)
    print(dict_palabra)


if __name__ == '__main__':
    main()
