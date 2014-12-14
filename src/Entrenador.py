__author__ = 'Grupo 7'
from src.Persona import *


class Entrenador(Persona):
    """ Clase Entrenador la cual hereda de Persona """

    def __init__(self, nombre, apellidos, dni, fecha_nac, pais_nac, licencia):
        """
        Constructor

        Inicializa el constructor de Entrenador, llamando a la clase Persona de la cual hereda
        :param nombre: nombre
        :param apellidos: apellidos
        :param dni: dni
        :param fecha_nac: fecha de nacimiento
        :param pais_nac: pais de nacimiento
        :param licencia: licencia del entrenador
        :type nombre: String
        :type apellidos: String
        :type dni: String
        :type fecha_nac: String
        :type pais_nac: String
        :type licencia: String
        :return:
        """
        Persona.__init__(self, nombre, apellidos, dni, fecha_nac, pais_nac)
        self.licencia = licencia

    def get_licencia(self):
        """
        Metodo consultor de la licencia

        Devuelve el codigo de la licencia
        :return: Codigo de la licencia
		:rtype: String
        """
        return self.licencia

    def set_licencia(self, licencia):
        """
        Metodo modificador de la licencia

        Modifica la licencia del entrenador
        :param licencia: licencia del entrenador
        :type licencia: String
        """
        self.licencia = licencia

    def mostrar_entrenador(self):
        """
        Muestra el entrenador

		Llama a la funcion str para mostrar un entrenador completo
        """
        cad = str(self)
        print (cad)

    def __str__(self):
        """
        Muestra el entrenador

		Devolvemos el entreneador en forma de cadena
		:return: Cadena con los datos del entrenador
		:rtype: String
        """
        return "ENTRENADOR: \n\tNombre: " + self.get_nombre() + "\n\tApellidos: " + self.get_apellidos() \
               + "\n\tDni: " + self.get_dni() + "\n\tFecha de nacimiento: " + self.get_fecha_nac() \
               + "\n\tPais de nacimiento: " + self.get_pais_nac() + "\n\tLicencia: " + self.get_licencia()