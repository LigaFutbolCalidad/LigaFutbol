__author__ = 'Grupo 7'
from src.Persona import *

class Entrenador(Persona):
    def __init__(self,nombre,apellidos,dni,fechaNac,paisNac,licencia):
        Persona.__init__(self,nombre,apellidos,dni,fechaNac,paisNac)
        self.licencia = licencia

    def get_licencia(self):
        return self.licencia

    def set_licencia(self,licencia):
        self.licencia = licencia

    def mostrar_entrenador(self):
        cad=str(self)
        print cad

    def __str__(self):
        return "ENTRENADOR: \n\tNombre: " + self.get_nombre() + "\n\tApellidos: " + self.get_apellidos() \
              + "\n\tDni: " + self.get_dni() + "\n\tFecha de nacimiento: " + self.get_fechaNac() \
              + "\n\tPais de nacimiento: " + self.get_paisNac() + "\n\tLicencia: " + self.get_licencia()