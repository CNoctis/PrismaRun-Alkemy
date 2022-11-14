def sumar(*args: float) -> float:
    """Suma todos los argumentos que recibe
    :param *args: Numeros enteros, flotantes o negativos
    :return: Resultado de la suma"""
    # Suma
    s = 0
    for arg in args:
        try:
            s += arg
        except Exception:
            return 'Error en la suma'
    return s


def restar(*args: float) -> float:
    """Resta todos los argumentos que recibe
    :param *args: Numeros enteros, flotantes o negativos
    :return: Resultado de la resta"""
    # Resta valor inicial
    try:
        r = float(args[0])
    except Exception:
        return 'Error en la resta'
    # Desde el elemento 1 hasta el n
    for arg in range(1, len(args)):
        try:
            r -= args[arg]
        except Exception:
            return 'Error en la resta'
    return r


def multiplicar(*args: float) -> float:
    """Multiplica todos los argumentos que recibe
    :param *args: Numeros enteros, flotantes o negativos
    :return: Resultado de la multiplicación"""
    # Multiplicación valor inicial
    try:
        m = float(args[0])
    except Exception:
        return 'Error en la multiplicación'
    # Desde el elemento 1 hasta el n
    for arg in range(1, len(args)):
        try:
            m *= float(args[arg])
        except Exception:
            return 'Error en la multiplicación'
    return m


def dividir(*args: float) -> float:
    """Divide todos los argumentos que recibe
    :param *args: Numeros enteros, floatantes o negativos
    :return: Resultaod de la división"""
    # Division valor inicial
    try:
        d = args[0]
    except Exception:
        return 'Error en división'
    # Desde el elemento 1 hasta n
    for arg in range(1, len(args)):
        try:
            d /= args[arg]
        except Exception:
            return 'Error en la división'
    return d
