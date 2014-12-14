__author__ = 'Grupo 7'


class Persona:
    def __init__(self, nombre, apellidos, dni, fecha_nac, pais_nac):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.fecha_nac = fecha_nac
        self.pais_nac = pais_nac

    def get_nombre(self):
        return self.nombre

    def get_apellidos(self):
        return self.apellidos

    def get_dni(self):
        return self.dni

    def get_fecha_nac(self):
        return self.fecha_nac

    def get_pais_nac(self):
        return self.pais_nac

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

    def set_dni(self, dni):
        self.dni = dni

    def set_fecha_nac(self, fecha_nac):
        self.fecha_nac = fecha_nac

    def set_pais_nac(self, pais_nac):
        self.pais_nac = pais_nac
