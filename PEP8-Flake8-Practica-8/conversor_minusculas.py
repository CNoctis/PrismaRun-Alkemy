import logging

logging.basicConfig(filename='./logs/result.log', encoding='utf-8',
                    level=logging.DEBUG, datefmt='%y-%m-%d %H:%M:%S',
                    format='%(asctime)s - %(levelname)s - %(message)s')


def minusculas(palabras: list) -> list:
    """
    Funcion encargada de relizar la conversión de palabras en minusculas
    :palabras: lista de palabras a convertir
    :return: Lista de palabras en minusculas
    """
    # Listas de palabras en minusculas
    palabras_m = []

    # Recorrer la lista de palabras a convertir
    for palabra in palabras:
        # Tomar registro de excepciones
        try:
            palabra_m = palabra.lower()
            palabras_m.append(palabra_m)
            logging.info(f'conversión exitosa: {palabra} ---> {palabra.lower()}')
        except Exception:
            palabra_m = palabra
            palabras_m.append(palabra_m)
            logging.error(f'conversion fallida: {palabra}')
    return palabras_m


def main():
    # Lista de palabras
    fruits = ['Frutilla', 'Melón', 'PERA', 99.6, 'NaranJA', 'mORa', 'NisPERo', 99]
    minusculas(fruits)


if __name__ == '__main__':
    main()
