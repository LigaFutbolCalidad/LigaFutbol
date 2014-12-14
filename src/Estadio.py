__author__ = 'Grupo 7'


class Estadio:
    """
    Representacion de un estadio de una liga
    """
    def __init__(self, nombre, ciudad, capacidad):
        """
        Constructor

        Inicializa el constructor de Estadio
        :param nombre: Nombre del estadio
        :type nombre: String
        :param ciudad: Ciudad del estadio
        :type ciudad: String
        :param capacidad: Capacidad del estadio
        :type capacidad: Integer
        """
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad
        self.nombre_equipo = None

    def get_nombre(self):
        """
        Metodo consultor del nombre del estadio

        Devuelve el nombre del estadio
        :return: Nombre del estadio
        :rtype: String
        """
        return self.nombre

    def get_ciudad(self):
        """
        Metodo consultor de la ciudad del estadio

        Devuelve la ciudad del estadio
        :return: Ciudad del estadio
        :rtype: String
        """
        return self.ciudad

    def get_capacidad(self):
        """
        Metodo consultor de la capacidad del estadio

        Devuelve la capacidad del estadio
        :return: Capacidad del estadio
        :rtype: String
        """
        return self.capacidad

    def set_nombre(self,nombre):
        """
        Metodo modificador del nombre del estadio

        Modifica el nombre del estadio
        :param nombre: Nombre del estadio
        :type nombre: String
        """
        self.nombre = nombre

    def set_ciudad(self,ciudad):
        """
        Metodo modificador de la ciudad del estadio

        Modifica la ciudad del estadio
        :param ciudad: Ciudad del estadio
        :type ciudad: String
        """
        self.ciudad = ciudad

    def set_capacidad(self,capacidad):
        """
        Metodo modificador de la capacidad del estadio

        Modifica la capacidad del estadio
        :param capacidad: Capacidad del estadio
        :type capacidad: String
        """
        self.capacidad = capacidad

    def get_nombre_equipo(self):
        """
        Metodo consultor del nombre del equipo que posee el estadio

        Devuelve el nombre del equipo
        :return: Nombre del equipo
        :rtype: String
        """
        return self.nombre_equipo

    def set_nombre_equipo(self, nombre_equipo):
        """
        Metodo modificador del nombre del equipo que posee el estadio

        Modifica el nombre del equipo
        :param nombre_equipo: Nombre del equipo
        :type nombre_equipo: String
        """
        self.nombre_equipo = nombre_equipo

    def mostrar_estadio(self):
        """
        Metodo que muestra los datos de la clase Estadio

        Muestra los datos del Estadio
        """
        cad=str(self)
        print (cad)

    def __str__(self):
        """
        Metodo que devuelve los datos del Estadio

        Devuelve los datos del Estadio y el nombre de su equipo dependiendo si lo tiene o no
        :return: datos del Estadio
        :rtype: String
        """
        if self.get_nombre_equipo() is None:
            return "ESTADIO: \n\tNombre: " + self.get_nombre() + "\n\tCiudad: " + self.get_ciudad() + \
                   "\n\tCapacidad: " + str(self.get_capacidad())
        else:
            return "ESTADIO: \n\tNombre: " + self.get_nombre() + "\n\tCiudad: " + self.get_ciudad() + \
                   "\n\tCapacidad: " + str(self.get_capacidad()) + "\n\tNombre del equipo: " + self.get_nombre_equipo()