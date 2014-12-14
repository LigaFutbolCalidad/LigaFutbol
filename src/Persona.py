__author__ = 'Grupo 7'


class Persona:
    """ Clase Persona """
    def __init__(self, nombre, apellidos, dni, fecha_nac, pais_nac):
        """
        Constructor

        Inicializa el constructor de Persona
        :param nombre: nombre
        :param apellidos: apellidos
		:param dni: dni
		:param fecha_nac: fecha de nacimiento
		:param fecha_nac: pais de nacimiento
        :type nombre: String
        :type apellidos: String
		:type dni: String
		:type fecha_nac: String
		:type pais_nac: String
        :return:
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.fecha_nac = fecha_nac
        self.pais_nac = pais_nac

    def get_nombre(self):
        """
        Metodo consultor del nombre

        Devuelve el nombre de la persona
        :return: Nombre de la persona
		:rtype: String
        """
        return self.nombre

    def get_apellidos(self):
        """
        Metodo consultor del apellido

        Devuelve el apellido de la persona
        :return: Apellido de la persona
		:rtype: String
        """
        return self.apellidos

    def get_dni(self):
        """
        Metodo consultor del dni

        Devuelve el dni de la persona
        :return: Dni de la persona
		:rtype: String
        """
        return self.dni

    def get_fecha_nac(self):
        """
        Metodo consultor de la fecha de nacimiento

        Devuelve la fecha de nacimiento de la persona
        :return: Fecha de nacimiento de la persona
		:rtype: String
        """
        return self.fecha_nac

    def get_pais_nac(self):
        """
        Metodo consultor del pais de nacimiento

        Devuelve el pais de nacimiento de la persona
        :return: Pais de nacimiento de la persona
		:rtype: String
        """
        return self.pais_nac

    def set_nombre(self, nombre):
        """
        Metodo modificador del nombre

        Modifica el nombre de la persona
        :param nombre: nombre
        :type nombre: String
        """
        self.nombre = nombre

    def set_apellidos(self, apellidos):
        """
        Metodo modificador de los apellidos

        Modifica los apellidos de la persona
        :param apellidos: apelldios
        :type apellidos: String
        """
        self.apellidos = apellidos

    def set_dni(self, dni):
        """
        Metodo modificador el dni

        Modifica el dni de la persona
        :param dni: dni
        :type dni: String
        """
        self.dni = dni

    def set_fecha_nac(self, fecha_nac):
        """
        Metodo modificador de la fecha nacimiento

        Modifica la fecha de nacimiento de la persona
        :param fecha_nac: fecha de nacimiento
        :type fecha_nac: String
        """
        self.fecha_nac = fecha_nac

    def set_pais_nac(self, pais_nac):
        """
        Metodo modificador del pais de nacimiento

        Modifica el pais de la persona
        :param pais_nac: pais de nacimiento
        :type pais_nac: String
        """
        self.pais_nac = pais_nac
