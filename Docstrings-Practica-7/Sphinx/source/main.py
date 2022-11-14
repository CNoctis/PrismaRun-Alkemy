from datetime import date


class empleados:
    """
    Employee class properties
    :param nombre: name
    :param apellido: name
    :param fecha_nacimiento: Date of Birth
    :param nro_dni: Document number"""
    
    def __init__(self, nombre: str, apellido: str,
                 fecha_nacimiento: str, nro_dni: int) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nro_dni = nro_dni

    def calculate_ege(self) -> int:
        """
        Calculate age based on date of birth
        :return: age
        :rtype: int"""
        # Division of the date in day, month, year
        date_birth = self.fecha_nacimiento.split('/')
        # Str to int conversion
        date_birth = list(map(lambda date_num: int(date_num), date_birth))
        # Current date
        today = date.today()
        # Calculate age
        age = today.year - date_birth[2] - ((today.month, today.day) <
                                            (date_birth[1], date_birth[0]))
        return age

    def introduce(self) -> str:
        """Make an employee presentation
        :return: Introduce myself
        :rtype: str"""

        return f"""Hola, soy {self.nombre} {self.apellido}.
        Nací el {self.fecha_nacimiento} y DNI es {self.nro_dni}"""
