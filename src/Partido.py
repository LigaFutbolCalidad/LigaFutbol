__author__ = 'Equipo de Calidad'


class Partido:
    """
    Representacion de un partido de una liga
    """
    def __init__(self, jornada, equipo_local, equipo_visitante):
        """
        Constructor

        Inicializa el constructor de Partido
        :param jornada: jornada del partido
        :param equipo_local: nombre del equipo local
		:param equipo_visitante: nombre del equipo visitante
        :type jornada: Integer
        :type equipo_local: String
		:type equipo_visitante: String
        """
        self.jornada = jornada
        self.equipoLocal = equipo_local
        self.equipoVisitante = equipo_visitante
        self.golesLocales = 0
        self.golesVisitantes = 0
        self.jugado = False

    def get_jornada(self):
        """
        Metodo consultor de la jornada

        Devuelve la jornada
        :return: Numero de la jornada
		:rtype: Integer
        """
        return self.jornada

    def get_equipo_local(self):
        """
        Metodo consultor del equipo local

        Devuelve el nombre del equipo local
        :return: Nombre del equipo local
		:rtype: String
        """
        return self.equipoLocal

    def get_equipo_visitante(self):
        """
        Metodo consultor del equipo visitante

        Devuelve el nombre del equipo visitante
        :return: Nombre del equipo visitante
		:rtype: String
        """
        return self.equipoVisitante

    def get_goles_locales(self):
        """
        Metodo consultor de los goles locales

        Devuelve el numero de goles marcados por el equipo local
        :return: Numero de goles del equipo local
		:rtype: Integer
        """
        return self.golesLocales

    def get_goles_visitantes(self):
        """
        Metodo consultor de los goles visitantes

        Devuelve el numero de goles marcados por el equipo visitante
        :return: Numero de goles del equipo visitante
		:rtype: Integer
        """
        return self.golesVisitantes

    def get_jugado(self):
        """
        Metodo consultor si el partido ha sido jugado o no

        Devuelveun booleano diciendo el estado del partido, si es jugado o no
        :return: Si el partido ha sido jugado o no
		:rtype: Boolean
        """
        return self.jugado

    def set_jornada(self, jornada):
        """
        Metodo modificador del partido jugado o no

        Modifica si el partido ha sido jugado
        :param jornada: jornada del partido
        :type jornada: Integer
        """
        self.jornada = jornada

    def set_equipo_local(self, equipo):
        """
        Metodo modificador del nombre del equipo local

        Modifica el nombre del equipo local
        :param equipo: nombre del equipo local
        :type equipo: String
        """
        self.equipoLocal = equipo

    def set_equipo_visitante(self, equipo):
        """
        Metodo modificador del nombre del equipo visitante

        Modifica el nombre del equipo visitante
        :param equipo: nombre del equipo visitante
        :type equipo: String
        """
        self.equipoVisitante = equipo

    def set_goles_locales(self, goles):
        """
        Metodo modificador de los goles del equipo local

        Modifica el numero de goles metidos por el equipo local
        :param goles: goles metidos por el equipo local
        :type goles: Integer
        """
        self.golesLocales = goles

    def set_goles_visitantes(self, goles):
        """
        Metodo modificador de los goles del equipo visitante

        Modifica el numero de goles metidos por el equipo visitante
        :param goles: goles metidos por el equipo visitante
        :type goles: Integer
        """
        self.golesVisitantes = goles

    def set_jugado(self, jug):
        """
        Metodo modificador de si el partido ha sido jugado o no

        Modifica si el partido ha sido jugado o no
        :param jug: True or False
        :type jug: bool
        """
        self.jugado = jug

    def mostrar_partido(self):
        """
        Metodo que muestra los datos de partido

        Muestra los datos del partido
        :var cad: recoge los datos del partido
        :type cad: String
        """
        cad = str(self)
        print (cad)

    def __str__(self):
        """
        Metodo que devuelve los datos del partido

        Devuelve los datos del partido
        :return: datos del partido
        :rtype: String
        """
        if not self.jugado:
            return "PARTIDO:\n\tJornada: " + str(
                self.get_jornada()) + "\n\tEquipo local: " + self.get_equipo_local() + "\n\tEquipo visitante: " \
                + self.get_equipo_visitante()
        else:
            return "PARTIDO:\n\tJornada: " + str(
                self.get_jornada()) + "\n\tEquipo local: " + self.get_equipo_local() + "\n\tEquipo visitante: " \
                + self.get_equipo_visitante() + "\n\tGoles local: " + str(
                self.get_goles_locales()) + "\n\tGoles visitante: " + str(self.get_goles_visitantes())