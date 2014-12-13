__author__ = 'Grupo 7'

class Persona:
    def __init__(self,nombre,apellidos,dni,fechaNac,paisNac):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.fechaNac = fechaNac
        self.paisNac = paisNac

    def get_nombre(self):
        return self.nombre

    def get_apellidos(self):
        return self.apellidos

    def get_dni(self):
        return self.dni

    def get_fechaNac(self):
        return self.fechaNac

    def get_paisNac(self):
        return self.paisNac

    def set_nombre(self,nombre):
        self.nombre = nombre

    def set_apellidos(self,apellidos):
        self.apellidos = apellidos

    def set_dni(self,dni):
        self.dni = dni

    def set_fechaNac(self,fechaNac):
        self.fechaNac = fechaNac

    def set_paisNac(self,paisNac):
        self.paisNac = paisNac
