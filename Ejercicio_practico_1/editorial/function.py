def info_lines(myfile: str) -> list:
    """Retorna la cantidad de renglones y su contenido
    myfile: directorio del archivo
    return: lista en formato[cantidad de renglones, contenido de los renglones]
    """
    # Abrimos el archivo
    with open(myfile, 'r', encoding='utf-8') as f:
        # Leer el archivo
        Content = f.read()
        # Se parar el texto por \n (Salto de lineas)
        CoList = Content.split("\n")
        # Contamos la cantidad de renglones según los elementos de la lista
        Counter = len(CoList)
        return [Counter, CoList]


def word_counter(list_words: list) -> dict:
    """Retorna la cantidad de palabras que contiene cada renglon
    list_words: Lista de palabras a analizar
    return: diccionario con la cantidad de palabras por renglon
    """
    # Diccionario de renglones y cantidad de palabras
    lines_row = {}
    # Corremos la lista y analizamos renglon por renglon
    for row in range(len(list_words)):
        # Lista de palabras en el renglon
        list_word = list_words[row].split(" ")
        # Cantidad de palabras en el renglon
        num_words = len(list_word)
        # Guardamos en el diccionario según el numero de renglon
        # la cantidad de palabras encontradas
        lines_row[row+1] = num_words
    return lines_row
