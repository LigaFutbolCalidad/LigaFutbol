__author__ = 'Equipo de Calidad'
from src.Persona import *


class Jugador(Persona):
    def __init__(self, nombre, apellidos, dni, fecha_nac, pais_nac, dorsal, posicion):
        Persona.__init__(self, nombre, apellidos, dni, fecha_nac, pais_nac)
        self.dorsal = dorsal
        self.posicion = posicion
        self.golesMarcados = 0

    def get_dorsal(self):
        return self.dorsal

    def get_posicion(self):
        return self.posicion

    def get_goles_marcados(self):
        return self.golesMarcados

    def set_dorsal(self, dorsal):
        self.dorsal = dorsal

    def set_posicion(self, posicion):
        self.posicion = posicion

    def set_goles_marcados(self, goles_marcados):
        self.golesMarcados = goles_marcados

    def incrementar_goles(self):
        self.golesMarcados += 1

    def mostrar_jugador(self):
        cad = str(self)
        print (cad)

    def __str__(self):
        return "JUGADOR: \n\tNombre: " + self.get_nombre() + "\n\tApellidos: " + self.get_apellidos() + "\n\tDni: " \
               + self.get_dni() + "\n\tFecha de nacimiento: " + self.get_fechaNac() + "\n\tPais de nacimiento: " \
               + self.get_paisNac() + "\n\tDorsal: " + str(self.get_dorsal()) + "\n\tPosicion de juego: " \
               + self.get_posicion()
