__author__ = 'Equipo de Calidad'
from src.Persona import *


class Jugador(Persona):
    """ Clase Jugador la cual hereda de Persona """
    def __init__(self, nombre, apellidos, dni, fecha_nac, pais_nac, dorsal, posicion):
        """
        Constructor

        Inicializa el constructor de Jugador, llamando a la clase Persona de la cual hereda
        :param nombre: nombre del jugador
        :param apellidos: apellidos del jugador
		:param dni: dni del jugador
		:param fecha_nac: fecha de nacimiento del jugador
		:param pais_nac: pais de nacimiento del jugador
		:param dorsal: dorsal del jugador
		:param posicion: posicion del jugador
        :type nombre: String
        :type apellidos: String
		:type dni: String
		:type fecha_nac: String
		:type pais_nac: String
		:type dorsal: Integer
		:type posicion: String
        """
        Persona.__init__(self, nombre, apellidos, dni, fecha_nac, pais_nac)
        self.dorsal = dorsal
        self.posicion = posicion
        self.golesMarcados = 0

    def get_dorsal(self):
        """
        Metodo consultor del dorsal

        Devuelve el dorsal del jugador
        :return: el dorsal del jugador
		:rtype: Integer
        """
        return self.dorsal

    def get_posicion(self):
        """
        Metodo consultor de la posicion

        Devuelve la posicion del jugador
        :return: Posicion del jugador en el campo
		:rtype: String
        """
        return self.posicion

    def get_goles_marcados(self):
        """
        Metodo consultor de los goles marcados

        Devuelve el numero de goles marcados
        :return: Goles marcados
		:rtype: Integer
        """
        return self.golesMarcados

    def set_dorsal(self, dorsal):
        """
        Metodo modificador del dorsal

        Modifica el dorsal del jugador
        :param dorsal: dorsal del jugador a cambiar
        :type dorsal: Integer
        """
        self.dorsal = dorsal

    def set_posicion(self, posicion):
        """
        Metodo modificador de la posicion

        Modifica la posicion del jugador
        :param posicion: posicion del jugador a cambiar
        :type posicion: String
        """
        self.posicion = posicion

    def set_goles_marcados(self, goles_marcados):
        """
        Metodo modificador de los goles marcados

        Modifica el numero de goles marcados
        :param goles_marcados: goles marcados a cambiar
        :type goles_marcados: Integer
        """
        self.golesMarcados = goles_marcados

    def incrementar_goles(self):
        """
        Metodo para incrementar los goles del jugador

        Incrementa los goles marcados por el jugador
        """
        self.golesMarcados += 1

    def mostrar_jugador(self):
        """
        Metodo que muestra los datos del jugador

        Muestra los datos del jugador
        :var cad: recoge los datos del jugador
        :type cad: String
        """
        cad = str(self)
        print (cad)

    def __str__(self):
        """
        Metodo que devuelve los datos del jugador

        Devuelve los datos del jugador
        :return: datos del jugador
        :rtype: String
        """
        return "JUGADOR: \n\tNombre: " + self.get_nombre() + "\n\tApellidos: " + self.get_apellidos() + "\n\tDni: " \
               + self.get_dni() + "\n\tFecha de nacimiento: " + self.get_fechaNac() + "\n\tPais de nacimiento: " \
               + self.get_paisNac() + "\n\tDorsal: " + str(self.get_dorsal()) + "\n\tPosicion de juego: " \
               + self.get_posicion()
