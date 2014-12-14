__author__ = 'Equipo de Calidad'


class Equipo:
    """
    Representacion de un equipo de una liga
    """
    def __init__(self, nombre, anio_creacion, ciudad):
        """
        Constructor

        Inicializa el constructor de Equipo
        :param nombre: nombre del equipo
        :param anio-creacion: anio de creacion del equipo
		:param ciudad: ciudad del equipo
        :type nombre: String
        :type anio-creacion: String
		:type ciudad: String
        """
        self.nombre = nombre
        self.anioCreacion = anio_creacion
        self.ciudad = ciudad
        self.puntos = 0
        self.golesFavor = 0
        self.golesContra = 0
        self.partidosGanados = 0
        self.partidosEmpatados = 0
        self.partidosPerdidos = 0
        self.estadio = None
        self.entrenador = None
        self.jugadores = []

    def get_nombre(self):
        """
        Metodo consultor del nombre del equipo

        Devuelve el nombre del equipo
        :return: Nombre del equipo
		:rtype: String
        """
        return self.nombre

    def get_anio_creacion(self):
        """
        Metodo consultor del anio de creacion

        Devuelve el anio de creacion del equipo
        :return: Anio de creacion del equipo
		:rtype: Integer
        """
        return self.anioCreacion

    def get_ciudad(self):
        """
        Metodo consultor de la ciudad

        Devuelve la ciudad del equipo
        :return: Ciudad del equipo
		:rtype: String
        """
        return self.ciudad

    def get_puntos(self):
        """
        Metodo consultor de los puntos del equipo

        Devuelve los puntos que tiene el equipo
        :return: Puntos del equipo
		:rtype: Integer
        """
        return self.puntos

    def get_goles_favor(self):
        """
        Metodo consultor de los goles a favor del equipo

        Devuelve los goles a favor del equipo
        :return: Goles a favor
		:rtype: Integer
        """
        return self.golesFavor

    def get_goles_contra(self):
        """
        Metodo consultor de los goles en contra del equipo

        Devuelve los goles en contra del equipo
        :return: Goles en contra
		:rtype: Integer
        """
        return self.golesContra

    def get_partidos_ganados(self):
        """
        Metodo consultor de los partidos ganados del equipo

        Devuelve el numero de partidos ganados del equipo
        :return: Partidos ganados
		:rtype: Integer
        """
        return self.partidosGanados

    def get_partidos_perdidos(self):
        """
        Metodo consultor de los partidos perdidos del equipo

        Devuelve el numero de partidos perdidos del equipo
        :return: Partidos perdidos
		:rtype: Integer
        """
        return self.partidosPerdidos

    def get_partidos_empatados(self):
        """
        Metodo consultor de los partidos empatados del equipo

        Devuelve el numero de partidos empatados del equipo
        :return: Partidos empatados
		:rtype: Integer
        """
        return self.partidosEmpatados

    def get_estadio(self):
        """
        Metodo consultor del estadio del equipo

        Devuelve el estadio completo
        :return: estadio del equipo
		:rtype: Estadio
        """
        return self.estadio

    def get_entrenador(self):
        """
        Metodo consultor del entrenador del equipo

        Devuelve el entrenador completo
        :return: entrenador del equipo
		:rtype: Entrenador
        """
        return self.entrenador

    def get_jugadores(self):
        """
        Metodo consultor de la lista de jugadores

        Devuelve la lista completa con todos los jugadores que tiene el equipo
        :return: Lista de jugadores
		:rtype: Jugadores[]
        """
        return self.jugadores

    def set_nombre(self, nombre):
        """
        Metodo modificador del nombre del equipo

        Modifica el nombre del equipo
        :param nombre: nombre del equipo
        :type nombre: String
        """
        self.nombre = nombre

    def set_anio_creacion(self, anio_creacion):
        """
        Metodo modificador del anio de creacion del equipo

        Modifica el anio de creacion del equipo
        :param anio_creacion: anio de creacion del equipo
        :type anio_creacion: Integer
        """
        self.anioCreacion = anio_creacion

    def set_ciudad(self, ciudad):
        """
        Metodo modificador de la ciudad del equipo

        Modifica la ciudad del equipo
        :param ciudad: ciudad del equipo
        :type ciudad: String
        """
        self.ciudad = ciudad

    def set_puntos(self, puntos):
        """
        Metodo modificador de los puntos del equipo

        Modifica los puntos del equipo
        :param puntos: puntos del equipo
        :type puntos: Integer
        """
        self.puntos = puntos

    def set_goles_favor(self, goles_favor):
        """
        Metodo modificador de los goles a favor del equipo

        Modifica los goles a favor del equipo
        :param goles_favor: goles del equipo
        :type goles_favor: Integer
        """
        self.golesFavor = goles_favor

    def set_goles_contra(self, goles_contra):
        """
        Metodo modificador de los goles en contra del equipo

        Modifica los goles en contra del equipo
        :param goles_contra: goles en contra del equipo
        :type goles_contra: Integer
        """
        self.golesContra = goles_contra

    def set_partidos_ganados(self, partidos_ganados):
        """
        Metodo modificador de los partidos ganados del equipo

        Modifica los partidos ganados del equipo del equipo
        :param partidos_ganados: partidos ganados del equipo
        :type partidos_ganados: Integer
        """
        self.partidosGanados = partidos_ganados

    def set_partidos_perdidos(self, partidos_perdidos):
        """
        Metodo modificador de los partidos perdidos del equipo

        Modifica los partidos perdidos del equipo
        :param partidos_perdidos: partidos perdidos del equipo
        :type partidos_perdidos: Integer
        """
        self.partidosPerdidos = partidos_perdidos

    def set_partidos_empatados(self, partidos_empatados):
        """
        Metodo modificador de los partidos empatados del equipo

        Modifica los partidos empatados del equipo
        :param partidos_empatados: partidos empatados del equipo
        :type partidos_empatados: Integer
        """
        self.partidosEmpatados = partidos_empatados

    def incrementar_puntos(self, puntos):
        """
        Metodo que incrementa los puntos del equipo

        Incrementa los puntos del equipo tras un partido
        :param puntos: puntos a incrementar
        :type puntos: Integer
        """
        self.puntos += puntos

    def incrementar_goles_favor(self, goles):
        """
        Metodo que incrementa los goles a favor del equipo

        Incrementa los goles a favor del equipo tras un partido
        :param goles: goles a favor a incrementar
        :type goles: Integer
        """
        self.golesFavor += goles

    def incrementar_goles_contra(self, goles):
        """
        Metodo que incrementa los goles en contra del equipo

        Incrementa los goles en contra del equipo tras un partido
        :param goles: goles en contra a incrementar
        :type goles: Integer
        """
        self.golesContra += goles

    def incrementar_partidos_ganados(self):
        """
        Metodo que incrementa los partidos ganados del equipo

        Incrementa los partidos ganados del equipo
        """
        self.partidosGanados += 1

    def incrementar_partidos_empatados(self):
        """
        Metodo que incrementa los partidos empatados del equipo

        Incrementa los partidos empatados del equipo
        """
        self.partidosEmpatados += 1

    def incrementar_partidos_perdidos(self):
        """
        Metodo que incrementa los partidos perdidos del equipo

        Incrementa los partidos perdidos del equipo
        """
        self.partidosPerdidos += 1

    def asignar_estadio(self, estadio):
        """
        Metodo que asigna un estadio al equipo

        Asigna un estadio al equipo
        :param estadio: estadio a asignar al equipo
        :type estadio: Estadio
        """
        self.estadio = estadio
        print ("Estadio asignado al equipo correctamente.")

    def asignar_entrenador(self, entrenador):
        """
        Metodo que asigna un entrenador al equipo

        Asigna un entrenador al equipo
        :param entrenador: entrenador a asignar al equipo
        :type entrenador: Entrenador
        """
        self.entrenador = entrenador
        print ("Entrenador asignado al equipo correctamente.")

    def agregar_jugador(self, jugador):
        """
        Metodo que agrega un jugador al equipo

        Agrega un jugador al equipo
        :param jugador: jugador a agregar al equipo
        :type jugador: Jugador
        """
        if len(self.jugadores) < 11:
            if self.existe_jugador(jugador.get_dni()) is None:
                self.jugadores.append(jugador)
                print ("Jugador aniadido al equipo correctamente.")
            else:
                print ("El jugador ya pertenece al equipo.")
        else:
            print ("El equipo ya esta completo.")

    def pichichi_equipo(self):
        """
        Metodo que devuelve el pichichi del equipo

        Devuelve el jugador que mas goles ha metido del equipo
        :var maximo: maximo de goles marcados por un jugador
        :var pichichi: jugador que mas goles ha marcado del equipo
        :var i: jugadores del equipo
        :type maximo: Integer
        :type pichichi: Jugador
        :type i: Jugador
        :return: jugador del equipo que mas goles ha marcado
        :rtype: Jugador
        """
        maximo = 0
        pichichi = None
        for i in self.jugadores:
            if i.get_goles_marcados() > maximo:
                maximo = i.get_goles_marcados()
                pichichi = i
        return pichichi

    def consultar_jugador(self, jugador):
        """
        Metodo que muestra los datos de un jugador del equipo

        Muestra los datos de un jugador del equipo que se quiera consultar
        :param jugador: jugador a consultar del equipo
        :var j: jugador a consultar
        :type jugador: Jugador
        :type j: Jugador
        """
        j = self.existe_jugador(jugador.get_dni())
        if j is None:
            print ("El jugador no existe en el equipo.")
        else:
            j.mostrar_jugador()

    def existe_jugador(self, dni):
        """
        Metodo que comprueba si existe un jugador en el equipo

        Devuelve al jugador si existe en el equipo
        :param dni: dni del jugador a buscar en el equipo
        :var jugador: jugador del equipo
        :var j: jugador del equipo
        :type dni: String
        :type jugador: Jugador
        :type j: Jugador
        :return: devuelve el jugador si existe
        :rtype: Jugador
        """
        jugador = None
        for j in self.jugadores:
            if j.get_dni() == dni:
                jugador = j
        return jugador

    def listar_jugadores(self):
        """
        Metodo que muestra todos los jugadores del equipo

        Muestra una lista de los datos de los jugadores del equipo
        :var i: jugadores del equipo
        :type var: Jugador
        """
        if len(self.jugadores) > 0:
            for i in self.jugadores:
                i.mostrar_jugador()
        else:
            print ("No hay jugadores en el equipo.")

    def consultar_estadio(self):
        """
        Metodo que muestra los datos del estadio del equipo

        Mustra los datos del estadio del equipo
        """
        if self.estadio is not None:
            self.estadio.mostrar_estadio()
        else:
            print ("El equipo no tiene un estadio asignado.")

    def consultar_entrenador(self):
        """
        Metodo que muestra los datos del entrenador del equipo

        Mustra los datos del entrenador del equipo
        """
        if self.entrenador is not None:
            self.entrenador.mostrar_entrenador()
        else:
            print ("El equipo no tiene entrenador asignado.")

    def mostrar_equipo(self):
        """
        Metodo que muestra los datos del equipo

        Muestra los datos del equipo
        :var cad: recoge los datos del equipo
        :type cad: String
        """
        cad = str(self)
        print (cad)

    def __str__(self):
        """
        Metodo que devuelve los datos del equipo

        Devuelve los datos del equipo
        :return: datos del equipo
        :rtype: String
        """
        return "EQUIPO:\n\tNombre: " + self.get_nombre() + "\n\tAnio creacion: " + self.get_anio_creacion() \
               + "\n\tCiudad: " + self.get_ciudad() + "\n\tPuntos: " + str(self.get_puntos()) + "\n\tGoles a favor: " \
               + str(self.get_goles_favor()) + "\n\tGoles en contra: " + str(self.get_goles_contra()) \
               + "\n\tPartidos ganados: " + str(self.get_partidos_ganados()) + "\n\tPartidos perdidos: " \
               + str(self.get_partidos_perdidos()) + "\n\tPartidos empatados: " + str(self.get_partidos_empatados())

    def __cmp__(self, other):
        """
        Metodo que compara dos equipos

        Compara dos equipos por algun atributo
        :param other: el otro equipo con el que este se va a comparar
        :type other: Equipo
        :var res: resta de los puntos de este equipo y el pasado por parametros
        :return: resultado de la resta
        :rtype: Integer
        """
        res = self.get_puntos() - other.get_puntos()
        if res == 0:
            res = self.get_goles_favor() - other.get_goles_favor()
            if res == 0:
                res = other.get_goles_contra() - self.get_goles_contra()
        return res
