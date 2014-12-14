__author__ = 'Grupo 7'

from src.Partido import *
import random


class Liga:
    """ Clase Liga """

    def __init__(self, nombre, anio, pais):
        """
        Constructor

        Inicializa el constructor de Liga
        :param nombre: nombre
        :param anio: anio
		:param pais: pais
        :type nombre: String
        :type anio: Integer
		:type pais: String
        :return:
        """
        self.nombre = nombre
        self.anio = anio
        self.pais = pais
        self.equipos = []
        self.partidos = []

    def get_nombre(self):
        """
        Metodo consultor del nombre de la liga

        Devuelve el nombre de la liga
        :return: Nombre de la liga
		:rtype: String
        """
        return self.nombre

    def set_nombre(self, nombre):
        """
        Metodo modificador del nombre de la Liga

        Modifica el nombre de la liga
        :param nombre: nombre de la liga
        :type nombre: String
        """
        self.nombre = nombre

    def get_anio(self):
        """
        Metodo consultor del anio de la liga

        Devuelve el anio de la liga
        :return: Anio de la liga
		:rtype: Integer
        """
        return self.anio

    def set_anio(self, anio):
        """
        Metodo modificador del anio de la Liga

        Modifica el anio de la liga
        :param anio: anio de la liga
        :type anio: Integer
        """
        self.anio = anio

    def get_pais(self):
        """
        Metodo consultor del pais de la liga

        Devuelve el nombre del pais de la liga
        :return: Pais de la liga
		:rtype: Integer
        """
        return self.pais

    def set_pais(self, pais):
        """
        Metodo modificador del pais donde se juega la liga

        Modifica el pais de la liga
        :param pais: pais de la liga
        :type pais: String
        """
        self.pais = pais

    def get_equipos(self):
        """
        Metodo consultor de los equipos de la liga

        Devuelve la lista de equpos
        :return: Equipos del pais
		:rtype: Equipos
        """
        return self.equipos

    def existe_equipo(self, nombre):
        """
        Consulta si existe el equipo

        Busca en el listado de equipos de toda la liga
        :param nombre: nombre del equipo a buscar
        :type nombre: String
		:return: equipo
		:rtype: Equipo
        """
        equipo = None
        for e in self.equipos:
            if e.get_nombre() == nombre:
                equipo = e
        return equipo

    def aniadir_equipo(self, equipo):
        """
        Aniade un nuevo equipo

        Aniade un nuevo equipo a la liga
        :param equipo: equipo que deseamos aniadir
        :type equipo: Equipo
        """
        if self.existe_equipo(equipo.get_nombre()) is None:
            if len(self.equipos) == 4:
                print ("No se pueden aniadir mas equipos a la liga.")
            else:
                self.equipos.append(equipo)
                print ("Equipo aniadido correctamente.")
                if len(self.equipos) == 4:
                    self.crear_partidos()
        else:
            print ("El equipo ya esta aniadido en la liga.")

    def crear_partidos(self):
        """
        Metodo para crear los partidos

		Crea los partidos de forma aleatoria
        """
        i = 0
        for x in self.equipos:
            for y in self.equipos:
                equipo_local = x.get_nombre()
                equipo_visitante = y.get_nombre()
                if x.get_nombre() != y.get_nombre():
                    i += 1
                    p = Partido(i, equipo_local, equipo_visitante)
                    self.partidos.append(p)

    def listar_equipos(self):
        """
        Muestra el listado de equipos

        Muestra el listado de equipos que tiene la liga
        """
        for equipo in self.equipos:
            equipo.mostrar_equipo()

    @staticmethod
    def consultar_equipo(equipo):
        """
        Consulta el equipo

        LLama a la funcion mostrar_equipo para mostrar los datos de este
        :param equipo: nombre del equipo a mostrar
        :type equipo: String
        """
        equipo.mostrar_equipo()

    def listar_partidos(self):
        """
        Muestra el listado de partidos

        Muestra el listado de partidos que tiene la liga
        """
        for partido in self.partidos:
            partido.mostrar_partido()

    def consultar_calendario(self):
        """
        Consulta el calenmdario

        Consulta el calenmdario de los partidos no jugados
        """
        for partido in self.partidos:
            if not partido.get_jugado():
                partido.mostrar_partido()

    def consultar_clasificacion(self):
        """
        Consulta la clasificacion

        Consulta la clasifcicacion de todos los partidos jugados
        """
        self.get_equipos().sort(reverse=True)
        igual = "=" * 20
        lin = "-" * 53
        print ("\n" + igual + "CLASIFICACION" + igual)
        print ("EQUIPO\t\t\t\tG\tE\tP\tGF\tGC\tPUNTOS\n" + lin)
        for e in self.equipos:
            tam = len(e.get_nombre())
            space = " " * (20 - tam)
            cadena = e.get_nombre() + space + str(e.get_partidos_ganados()) + "\t" + str(e.get_partidos_empatados())
            cadena += "\t" + str(e.get_partidos_perdidos()) + "\t" + str(e.get_goles_favor())
            cadena += "\t" + str(e.get_goles_contra()) + "\t" + str(e.get_puntos())
            print (cadena)

    def existe_partido(self, jornada):
        """
        Consulta si existe el partido

        Busca en el listado de partidos de toda la liga
        :param jornada: nombre de la jornada que desea buscar
        :type jornada: String
		:return: partido
		:rtype: Partido
        """
        partido = None
        for p in self.partidos:
            if p.get_jornada() == jornada:
                partido = p
        return partido

    @staticmethod
    def consultar_partido(partido):
        """
        Consulta el partido

        LLama a la funcion mostrar_partido para mostrar los datos de este
        :param partido: partido a mostrar
        :type partido: String
        """
        partido.mostrar_partido()

    def jugar_partido(self):
        """
        Es el metodo principal, el cual genera los partidos de forma aleatoria

        Hace uso de varias funciones para dividir el codigo y ser mas sencillo de leer
        """
        jornada = input("Seleccione la jornada: ")
        p = self.existe_partido(jornada)
        if p is None:
            print ("La jornada no coincide con ninguna de la liga")
        else:
            if p.get_jugado():
                print ("El partido ya se ha jugado")
            else:
                local = self.existe_equipo(p.get_equipo_local())
                visitante = self.existe_equipo(p.get_equipo_visitante())
                p.mostrar_partido()

                goles_local = self.cofig_partido_local(local)
                goles_visitante = self.cofig_partido_visitante(visitante)

                local.incrementar_goles_contra(goles_visitante)
                visitante.incrementar_goles_contra(goles_local)

                if goles_local == goles_visitante:
                    local.incrementar_partidos_empatados()
                    visitante.incrementar_partidos_empatados()
                    local.incrementar_puntos(2)
                    visitante.incrementar_puntos(2)
                elif goles_local > goles_visitante:
                    local.incrementar_puntos(3)
                    local.incrementar_partidos_ganados()
                    visitante.incrementar_partidos_perdidos()
                else:
                    visitante.incrementar_puntos(3)
                    visitante.incrementar_partidos_ganados()
                    local.incrementar_partidos_perdidos()
                p.set_goles_locales(goles_local)
                p.set_goles_visitantes(goles_visitante)
                p.set_jugado(True)

    @staticmethod
    def cofig_partido_local(local):
        """
        Configura los datos del partido jugado del equipo local

        Aniade los goles al equipo, y a los jugadores
        :param local: equipo local
        :type local: Equipo
		:return: Numero de goles marcados
		:rtype: Integer
        """
        goles_local = -1
        while goles_local < 0:
            goles_local = input("Inserte los goles marcados del equipo local: ")
            if goles_local < 0:
                print ("Goles incorrectos")
        x = 1
        while x <= goles_local:
            dni = raw_input(
                "Inserte el dni del jugador que ha marcado el gol " + str(x) + " del equipo local: ")
            j = local.existe_jugador(dni)
            if j is None:
                print ("El jugador no existe")
            else:
                j.incrementar_goles()
                x += 1
        local.incrementar_goles_favor(goles_local)
        return goles_local

    @staticmethod
    def cofig_partido_visitante(visitante):
        """
        Configura los datos del partido jugado del equipo visitante

        Aniade los goles al equipo, y a los jugadores
        :param visitante: equipo visitante
        :type visitante: Equipo
		:return: Numero de goles marcados
		:rtype: Integer
        """
        goles_visitante = -1
        while goles_visitante < 0:
            goles_visitante = input("Inserte los goles marcados del equipo visitante: ")
            if goles_visitante < 0:
                print ("Goles incorrectos")
        x = 1
        while x <= goles_visitante:
            dni = raw_input(
                "Inserte el dni del jugador que ha marcado el gol " + str(x) + " del equipo visitante:")
            j = visitante.existe_jugador(dni)
            if j is None:
                print ("El jugador no existe")
            else:
                j.incrementar_goles()
                x += 1
        visitante.incrementar_goles_favor(goles_visitante)
        return goles_visitante

    def jugar_partidos_auto(self):
        """
        Realiza las operaciones para que se jueguen los partidos de forma automatica

        Se juegan los partidos
        """
        for p in self.partidos:
            if not p.get_jugado():
                g1 = random.randint(0, 5)
                l = self.existe_equipo(p.get_equipo_local())
                p.set_goles_locales(g1)
                for i in range(0, g1):
                    indice = random.randint(0, len(l.get_jugadores()) - 1)
                    l.get_jugadores()[indice].incrementar_goles()

                g2 = random.randint(0, 5)
                v = self.existe_equipo(p.get_equipo_visitante())
                p.set_goles_visitantes(g2)
                for i in range(0, g2):
                    indice = random.randint(0, len(v.get_jugadores()) - 1)
                    v.get_jugadores()[indice].incrementar_goles()

                l.incrementar_goles_favor(g1)
                v.incrementar_goles_favor(g2)
                l.incrementar_goles_contra(g2)
                v.incrementar_goles_contra(g1)

                if g1 == g2:
                    l.incrementar_puntos(1)
                    v.incrementar_puntos(1)
                    l.incrementar_partidos_empatados()
                    v.incrementar_partidos_empatados()
                elif g1 > g2:
                    l.incrementar_puntos(3)
                    l.incrementar_partidos_ganados()
                    v.incrementar_partidos_perdidos()
                else:
                    v.incrementar_puntos(3)
                    v.incrementar_partidos_ganados()
                    l.incrementar_partidos_perdidos()

                p.set_jugado(True)

    def consultar_mejor_estadio(self):
        """
        Consulta el estadio con mayor capacidad

        Realiza una busqueda entre todos los estadios de cada equipo, mostrando el que mas capacidad dispone
        """
        capacidad_estadio = 0
        mayor_estadio = None
        for equipo in self.equipos:
            estadio = equipo.get_estadio()
            if estadio.get_capacidad() > capacidad_estadio:
                capacidad_estadio = estadio.get_capacidad()
                mayor_estadio = estadio
        if mayor_estadio is None:
            print ("Ningun equipo tiene estadio")
        else:
            print ("El estadio con mayor capacidad es: " + mayor_estadio.get_nombre())

    def pichichi_liga(self):
        """
        Consulta el pichichi de la liga

        Hace uso del metodo recorrer_equipos para buscar el pichichi de la liga
        """
        if len(self.equipos) > 0:
            pichichi = self.recorrer_equipos()
            if pichichi is not None:
                print ("El pichichi de la liga con " + str(pichichi.get_goles_marcados()) + " goles marcados es: ")
                pichichi.mostrar_jugador()
            else:
                print ("La liga no tiene pichichi aun.")
        else:
            print ("La liga no tiene equipos aun.")

    def recorrer_equipos(self):
        """
        Recorre el listado de equipos

        Busca en el listado de equipos el pichichi de la liga
		:return: pichichi
		:rtype: Jugador
        """
        goles = 0
        pichichi = None
        for equipo in self.equipos:
            jugador = equipo.pichichi_equipo()
            if jugador is not None and jugador.get_goles_marcados() > goles:
                goles = jugador.get_goles_marcados()
                pichichi = jugador
        return pichichi

    def listar_pichichis_equipos(self):
        """
        Aparece un listado con los pichichis de los equipos

        Recorre todos los equipos, mostrando los pichichis de cada equipo
        """
        for e in self.get_equipos():
            if e.pichichi_equipo() is not None:
                e.pichichi_equipo().mostrar_jugador()

    def mostrar_liga(self):
        """
        Muestra los datos de la liga

        Mestra todos los datos de la liga, haciendo uso de la funcion str
        """
        cad = str(self)
        print (cad)

    def __str__(self):
        """
        Muestra los datos de la liga

        Muestra los atributos de la liga
		:return: Cadena formada por los datos de la liga
		:rtype: String
        """
        return "LIGA: \n\tNombre: " + self.nombre + "\n\tAnio: " + str(self.anio) + "\n\tPais: " + self.pais