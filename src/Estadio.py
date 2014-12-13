__author__ = 'Grupo 7'

class Estadio:
    def __init__(self,nombre,ciudad,capacidad):
        self.nombre=nombre
        self.ciudad=ciudad
        self.capacidad=capacidad
        self.nombreEquipo = None

    def get_nombre(self):
        return self.nombre

    def get_ciudad(self):
        return self.ciudad

    def get_capacidad(self):
        return self.capacidad

    def set_nombre(self,nombre):
        self.nombre=nombre

    def set_ciudad(self,ciudad):
        self.ciudad=ciudad

    def set_capacidad(self,capacidad):
        self.capacidad=capacidad

    def get_nombreEquipo(self):
        return self.nombreEquipo

    def set_nombreEquipo(self,nombreEquipo):
        self.nombreEquipo = nombreEquipo

    def mostrar_estadio(self):
        cad=str(self)
        print cad

    def __str__(self):
        if self.get_nombreEquipo() == None:
            return "ESTADIO: \n\tNombre: " + self.get_nombre() + "\n\tCiudad: " + self.get_ciudad() + "\n\tCapacidad: " \
               + str(self.get_capacidad())
        else:
            return "ESTADIO: \n\tNombre: " + self.get_nombre() + "\n\tCiudad: " + self.get_ciudad() + "\n\tCapacidad: " \
               + str(self.get_capacidad()) + "\n\tNombre del equipo: " + self.get_nombreEquipo()