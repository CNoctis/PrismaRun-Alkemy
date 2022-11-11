"""
Esta es una clase de pruebas para implementar Sphinx
"""
class Teacher:
    """
    Clase que contiene las propiedades de un profesor
    :param first_name: Primer nombre del profesor
    :param last_name: Apellido del profesor
    """
    def __init__(self, first_name:str , last_name:str , age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        """
        Esta función no recibe parámetros
        :return: Nombre y apellido del profesor
        :rtype: string
        """
        return f"{self.first_name} {self.last_name}"
        
    def introduce(self):
        """
        Esta función no recibe parámetros
        :return: Presentación del profesor. Nombre,
        apellido y edad
        :rtype: string
        """
        return f"Hi. I'm {self.first_name}{self.last_name}. I'm {self.age} years old."